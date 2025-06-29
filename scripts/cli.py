from app.rag.rag_pipeline import get_qa_chain

qa = get_qa_chain()
while True:
    q = input("Ask a question (or 'exit'): ")
    if q.lower() == "exit":
        break
    result = qa(q)
    print("\nAnswer:", result["result"])
    print("Sources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata)
