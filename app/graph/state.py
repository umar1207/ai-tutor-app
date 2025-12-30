from typing import TypedDict, List
from langchain_core.documents import Document


class GraphState(TypedDict):
    query: str
    retrieved_docs: List[Document]
    agent_type: str
    result: dict | str
