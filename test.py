from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama

from langchain.chains import RetrievalQA
import os

# ---------- CONFIG ----------
DATA_DIR = "data"
VECTOR_DB_DIR = "embeddings"


# ---------- STEP 1: LOAD DOCUMENTS ----------
docs = []

# Load PDF
pdf_path = os.path.join(DATA_DIR, "userguide.pdf")
pdf_loader = PyMuPDFLoader(pdf_path)
docs.extend(pdf_loader.load())

# Load Markdown file
md_path = os.path.join(DATA_DIR, "CFM_OAM.md")
md_loader = TextLoader(md_path, encoding='utf-8')
docs.extend(md_loader.load())

print(f"Loaded {len(docs)} documents")

# ---------- STEP 2: SPLIT INTO CHUNKS ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
print(f"Split into {len(chunks)} chunks")

# ---------- STEP 3: EMBEDDINGS + VECTOR STORE ----------
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_function,
    persist_directory=VECTOR_DB_DIR
)

vectordb.persist()
print("✅ Vector database created and saved!")


# ---------- STEP 4: QUERY PIPELINE WITH OLLAMA ----------
llm = Ollama(model="qwen3")  # or "mistral" / "phi3" etc.

retriever = vectordb.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# ---------- STEP 5: ASK QUESTIONS ----------
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    result = qa_chain.invoke({"query": query})
    print("\n🧠 Answer:")
    print(result["result"])

    print("\n📚 Sources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source", "Unknown file"))