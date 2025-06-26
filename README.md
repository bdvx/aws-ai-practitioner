# 🎨 Museum RAG Demo (Retrieval-Augmented Generation)

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using OpenAI's GPT-3.5 model and a collection of museum documents. The system allows users to ask natural language questions and receive answers grounded in curated museum-related content.

---

## 📁 Project Structure

```
.
├── collection/              # ⚠️ Not committed – folder with source documents (.json)
├── .env                     # ⚠️ Not committed – contains OpenAI API key
├── app/
│   ├── data/
│   │   └── loader.py        # Loads .txt files from the `collection/` directory
│   └── rag/
│       ├── splitter.py      # Splits documents into manageable text chunks
│       ├── vectorstore.py   # Creates/loads a Chroma vector index with SentenceTransformer
│       └── rag_pipeline.py  # Combines retriever and OpenAI LLM into a RetrievalQA chain
├── scripts/
│   ├── ingest.py            # Loads, splits, and indexes documents
│   └── cli.py               # Runs a simple CLI-based Q&A loop
└── requirements.txt         # Python dependencies
```

---

## 🧰 Requirements

- Python 3.10 or higher
- OpenAI API key
- Internet connection (for downloading models and calling APIs)

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/museum-rag-demo.git
   cd museum-rag-demo
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Create `.env` file**
   Add your OpenAI API key to a `.env` file in the project root:
   ```
   OPENAI_API_KEY=sk-...
   ```

4. **Add documents to `collection/` folder**
   Place museum-related `.txt` files in a folder named `collection` (next to `scripts/`).  
   > ⚠️ This folder is not committed due to data size.

---

## 🧠 Run Document Ingestion

Before you can ask questions, build the vector index:

```bash
python scripts/ingest.py
```

This will:
- Load documents from `collection/`
- Split them into chunks
- Embed and store them using Chroma

---

## 💬 Start the CLI Q&A Bot

Once the vector index is ready, start the interactive question-answering loop:

```bash
python scripts/cli.py
```

Example prompt:
```
Ask a question (or 'exit'): Show me American paintings from the 19th century
```

You’ll get:
- A concise GPT-generated answer
- Source document metadata used to answer it

---

## ❌ No Uvicorn/FastAPI Required

This is a **CLI-only demo** – no need to run a web server.

If needed later, you can wrap the RAG logic into a FastAPI app and serve via `uvicorn`.

---

## 🔒 Notes

- `.env` is not committed for security reasons.
- `collection/` is excluded due to file size limits.
- Model: `gpt-3.5-turbo-instruct` (used via `langchain.llms.OpenAI`).

---

## 🧾 License

This project is for educational/demo purposes. Please ensure your OpenAI usage complies with their terms of service.

---
