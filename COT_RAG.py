# rag_with_cot_api.py
import os
import json
import requests
from pathlib import Path
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# ------------------------------------------------- CONFIG -------------------------------------------------
BASE_DIR = Path(__file__).parent
VECTOR_DB_DIR = BASE_DIR / "embeddings"

PDF_FILES = [BASE_DIR / f for f in ["y1731.pdf", "8021ag-2007.pdf"]]
MD_FILES  = [BASE_DIR / f for f in ["CFM_OAM.md", "cfm-debugging.md", "dataset.csv", "product.txt"]]

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
TOP_K = int(os.getenv("TOP_K", "3"))

# ------------------------------------------------- SYSTEM PROMPT -------------------------------------------------
SYSTEM_PROMPT = """You are a helpful, precise assistant specialized in using provided documents (CONTEXT) plus your internal knowledge when necessary.
Rules:
1. ALWAYS consult the CONTEXT block first for factual answers. If the CONTEXT contains explicit text that answers the question, answer only from that information.
2. If the CONTEXT is insufficient or the user asks for theoretical/explanatory content, you may use your internal knowledge to answer — but mark which parts come from CONTEXT and which parts are from your internal knowledge.
3. Do NOT reveal raw internal chain-of-thought. Instead provide a brief "Reasoning summary" (2–4 lines) that explains the key steps or assumptions you used to reach the conclusion.
4. For any command / RPC / exact-value request: prefer exact context matches. If the exact value or command is not present in CONTEXT, reply with "NOT FOUND IN CONTEXT" and then, only if the user asked to, provide a best-effort answer using internal knowledge labeled as such.
5. When you cite CONTEXT, include the document id or filename and a short quote or line reference.
6. When you produce code, commands, or RPC responses, return them in fenced code blocks and mark them clearly as `EXACT FROM CONTEXT` if pulled verbatim; otherwise label as `DERIVED` or `INTERNAL_KNOWLEDGE`.
7. Also use multiple context when producing RPC and LightSpan RPC to give correct RPC, Check it multiple times majorly when it is asked to fetch RPC
8. Do not disclose the internal documents in response.
"""

# ------------------------------------------------- PROMPT BUILDER -------------------------------------------------
def build_prompt(retrieved_docs: List, question: str) -> str:
    ctx_parts = []
    for i, d in enumerate(retrieved_docs, start=1):
        src = d.metadata.get("source", f"doc_{i}")
        snippet = d.page_content.strip()
        ctx_parts.append(f"[Document {i}: {src}]\n{snippet}\n")
    ctx_block = "\n\n".join(ctx_parts)

    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        "CONTEXT:\n========\n"
        f"{ctx_block}\n"
        "END_CONTEXT\n========\n\n"
        "INSTRUCTIONS:\n"
        "1) Use the CONTEXT above as primary source for factual answers. If CONTEXT contains the direct answer, use it verbatim and label EXACT FROM CONTEXT.\n"
        "2) If the CONTEXT does not contain an answer, you may answer using internal knowledge, but label that content as INTERNAL_KNOWLEDGE.\n"
        "3) Provide:\n"
        " a) A short direct answer (1-3 sentences).\n"
        " b) If an exact command or RPC is requested and is found verbatim in the CONTEXT, show it in a fenced code block labeled EXACT FROM CONTEXT. If not present, print NOT FOUND IN CONTEXT.\n"
        " c) A short 'Reasoning summary' (2-4 lines). Do NOT reveal chain-of-thought.\n"
        " d) A 'Sources' list referencing the document names and quoted snippets.\n\n"
        f"QUESTION:\n{question}\n"
    )
    return prompt

# ------------------------------------------------- OLLAMA CALL -------------------------------------------------
def call_ollama(prompt: str, model: str = OLLAMA_MODEL, stream: bool = False, timeout: int = 300) -> str:
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": stream}
    resp = requests.post(url, json=payload, stream=stream, timeout=timeout)
    if resp.status_code >= 400:
        raise RuntimeError(f"Ollama error {resp.status_code}: {resp.text[:500]}")
    if stream:
        out = ""
        for line in resp.iter_lines():
            if not line: continue
            data = json.loads(line.decode("utf-8"))
            if "response" in data: out += data["response"]
            if data.get("done"): break
        return out
    else:
        return resp.json().get("response", "")

# ------------------------------------------------- GLOBAL -------------------------------------------------
retriever: Optional[Any] = None   # will be filled in lifespan

# ------------------------------------------------- LIFESPAN -------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    global retriever

    # ---------- Load raw documents ----------
    docs = []
    for p in PDF_FILES:
        if p.is_file():
            docs.extend(PyMuPDFLoader(str(p)).load())
        else:
            print(f"Warning: PDF not found: {p}")
    for p in MD_FILES:
        if p.is_file():
            docs.extend(TextLoader(str(p), encoding="utf-8").load())
        else:
            print(f"Warning: MD not found: {p}")

    if not docs:
        raise RuntimeError("No PDF/MD files found – place them next to the script.")

    # ---------- Chunk ----------
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    # ---------- Embeddings ----------
    embedder = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

    # ---------- Persist / Load ----------
    persist_dir = str(VECTOR_DB_DIR)
    if VECTOR_DB_DIR.exists() and any(VECTOR_DB_DIR.iterdir()):
        print(f"Loading existing Chroma DB from {persist_dir}")
        vectordb = Chroma(persist_directory=persist_dir, embedding_function=embedder)
    else:
        print(f"Creating new Chroma DB at {persist_dir}")
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embedder,
            persist_directory=persist_dir,
        )
        # .persist() is no longer needed with Chroma >=0.4
        # vectordb.persist()

    # ---------- Retriever ----------
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})
    print(f"Vector DB ready – {len(chunks)} chunks, top_k={TOP_K}")

    yield   # <--- app runs here

    print("Shutting down...")

# ------------------------------------------------- FASTAPI APP -------------------------------------------------
app = FastAPI(
    title="RAG + COT Ollama API",
    description="Ask questions, get answers backed by your PDF/MD docs.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------- HEALTH -------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "ollama_host": OLLAMA_HOST,
        "ollama_model": OLLAMA_MODEL,
        "top_k": TOP_K,
    }

# ------------------------------------------------- MANUAL VALIDATION HELPERS -------------------------------------------------
def _validate_query_payload(data: Dict[str, Any]) -> tuple[str, int]:
    """Return (question, top_k) – raises HTTPException on invalid input."""
    if not isinstance(data, dict):
        raise HTTPException(status_code=400, detail="Request body must be JSON object")

    question = data.get("question")
    if not isinstance(question, str) or not question.strip():
        raise HTTPException(status_code=400, detail="Field 'question' must be a non-empty string")

    top_k = data.get("top_k")
    if top_k is not None:
        if not isinstance(top_k, int) or top_k <= 0:
            raise HTTPException(status_code=400, detail="Field 'top_k' must be a positive integer")
        top_k = min(top_k, 50)   # optional upper bound
    else:
        top_k = TOP_K

    return question.strip(), top_k

# ------------------------------------------------- QUERY -------------------------------------------------
@app.post("/query")
async def query(request: Request):
    """
    Expected JSON:
    {
        "question": "string",
        "top_k": int (optional)
    }
    """
    if retriever is None:
        raise HTTPException(status_code=500, detail="Retriever not initialized")

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    try:
        question, k = _validate_query_payload(payload)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Validation error: {e}")

    retrieved = retriever.invoke(question)[:k]

    prompt = build_prompt(retrieved, question)
    answer = call_ollama(prompt, model=OLLAMA_MODEL, stream=False)

    sources = [
        {
            "id": i + 1,
            "source": d.metadata.get("source", f"doc_{i+1}"),
            "snippet": d.page_content.strip()[:800],
        }
        for i, d in enumerate(retrieved)
    ]

    return {
        "answer": answer,
        "sources": sources,
    }

# ------------------------------------------------- SCRIPT RUN -------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")