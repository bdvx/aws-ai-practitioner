from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    input_docs = [Document(page_content=doc["text"], metadata=doc["metadata"]) for doc in documents]
    return splitter.split_documents(input_docs)