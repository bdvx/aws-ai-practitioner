from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.rag.vectorstore import load_chroma_index
from dotenv import load_dotenv
load_dotenv()

def get_qa_chain():
    vectordb = load_chroma_index()
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a museum guide. Use the below context to answer the question. Be concise and cite sources if possible.

Context:
{context}

Question:
{question}

Answer:"""
    )
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0, model="text-embedding-ada-002"),
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=True
    )
