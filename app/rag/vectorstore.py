from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def create_chroma_index(documents, persist_directory="db"):
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents, embedding, persist_directory=persist_directory)
    vectordb.persist()
    return vectordb

def load_chroma_index(persist_directory="db"):
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)
