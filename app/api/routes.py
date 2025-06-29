from fastapi import APIRouter, HTTPException
from app.schemas.question import QuestionRequest
from app.rag.rag_pipeline import get_qa_chain
import logging

router = APIRouter()
qa_chain = get_qa_chain()

@router.post("/ask")
def ask_question(req: QuestionRequest):
    try:
        result = qa_chain(req.question)
        return {
            "question": req.question,
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]]
        }
    except Exception as e:
        logging.exception("Error answering question")
        raise HTTPException(status_code=500, detail=str(e))
