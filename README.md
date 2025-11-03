# 🧠 Customer Tech Support Assistant
**AI-Powered Knowledge Retrieval and Chat System**

The **Customer Tech Support Assistant** is an intelligent AI-powered chatbot designed to assist both **customers** and **tech support engineers** by retrieving relevant information from internal documents and providing accurate, context-aware responses using **Mistral LLM** served through **Ollama**.

---

## 🏗️ System Architecture


The system is composed of the following layers:

- **User Layer** – Interfaces for customers and tech support engineers.  
- **Frontend Layer** – React-based chat interface with login and chat windows.  
- **Backend Layer** – Python REST API that handles queries, embeddings, and response generation.  
- **AI Model Layer** – Mistral LLM served locally via Ollama for generating intelligent responses.  
- **Knowledge Layer** – ChromaDB vector store holding embeddings of domain-specific documents.  

---

## ⚙️ Setup and Run Instructions

Follow these steps to set up and run the complete application locally:

### 🧩 1. Install Ollama and Download the Mistral Model
Download and install Ollama from the [official website](https://ollama.ai/).  
Then, pull the **Mistral model**:

```bash
ollama pull mistral
```

---

### 🚀 2. Start Ollama Server

Serve the model locally:

```bash
ollama serve
```

This will run the Ollama model service locally for inference.

---

### 🐍 3. Set Up and Run the Backend

Install Python dependencies:

```bash
pip install -r req.txt
```

Then run the backend server:

```bash
python COT_RAG.py
```

This starts the REST API that handles query processing, vector embeddings, and model interaction.

---

### 💻 4. Set Up and Run the Frontend

Navigate to the frontend directory:

```bash
cd cust-tech-support
```

Make sure **Node.js** is installed. Then install dependencies and start the app:

```bash
npm install
npm run dev
```

---

### 🌐 5. Access the Application

Once both backend and frontend are running, open your browser and go to:

👉 **http://localhost:5173**

You’ll see the login window — after authentication, you can start interacting with the AI assistant via the chat window.

---

## 🧠 Features

- 🔍 **AI-Powered Query Resolution** — Answers technical and troubleshooting queries.  
- 🧩 **Vector-Based Knowledge Retrieval** — Fetches relevant context from stored embeddings using **ChromaDB**.  
- 🗂️ **Knowledge Base Categorization** — Organized into Provisioning, Troubleshooting, Standards, and Historical Issues KBs.  
- ⚡ **Real-Time Responses** — Seamless frontend-backend communication via REST API.  
- 🔐 **Authenticated Access** — Separate roles for Customers and Support Engineers.

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Vite, TailwindCSS |
| **Backend** | Python (Flask / FastAPI) |
| **AI Model Layer** | Ollama + Mistral LLM |
| **Vector Database** | ChromaDB |
| **Data Sources** | Provisioning Docs, Troubleshooting Docs, Standards, JIRA DB |
| **Package Manager** | npm, pip |

---

## 🔮 Future Enhancements

- 🔗 Integrate live JIRA issue retrieval and status updates.  
- 📊 Add analytics dashboard for query patterns and response accuracy.  
- 🧠 Implement feedback-based continual model improvement.  
- 🧾 Extend support for multi-language queries and responses.  
- 🧑‍💼 Add role-based permissions and team chat features.

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.
