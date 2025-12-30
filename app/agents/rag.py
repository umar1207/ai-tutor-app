# app/agents/rag.py

from typing import Dict
from app.documents.processor import DocumentProcessor


class RAGAgent:
    """
    Responsible ONLY for retrieval.
    Does not call LLM.
    Does not format prompts.
    """

    def __init__(self, document_processor: DocumentProcessor, k: int = 4):
        self.document_processor = document_processor
        self.k = k

    def retrieve(self, state: Dict) -> Dict:
        """
        Input state:
        {
            "query": str,
            ...
        }

        Output state:
        {
            "query": str,
            "retrieved_docs": List[Document],
            ...
        }
        """
        query = state["query"]

        retriever = self.document_processor.retriever(k=self.k)
        docs = retriever.invoke(query)

        state["retrieved_docs"] = docs
        return state
