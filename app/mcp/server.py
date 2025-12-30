from mcp.server.fastmcp import FastMCP
from app.documents.processor import DocumentProcessor
from app.llm.openai_llm import OpenAILLM
from app.graph.workflow import build_graph

mcp = FastMCP("Document Learning MCP")

llm_provider = OpenAILLM()

processor = DocumentProcessor(llm_provider.embeddings())
graph = build_graph(processor.retriever(), llm_provider.chat())


@mcp.tool()
def ingest_document(content: str, source: str):
    """Upload and index a document"""
    return {"chunks": processor.ingest(content, source)}


@mcp.tool()
def query_document(query: str, agent_type: str = "qa"):
    """Query documents using QA / Quiz / Learning mode"""
    result = graph.invoke({
        "query": query,
        "agent_type": agent_type
    })
    return result["result"]
