from app.data.loader import load_documents_from_folder
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_chroma_index

def run_ingestion():
    docs = load_documents_from_folder("collection")
    print(f"Loaded {len(docs)} documents")

    chunks = split_documents(docs)
    print(f"Split into {len(chunks)} chunks")

    for i, c in enumerate(chunks[:3]):
        print(f"[{i}] {c.page_content[:100]}...")

    create_chroma_index(chunks)

if __name__ == "__main__":
    run_ingestion()
