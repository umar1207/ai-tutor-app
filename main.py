from app.llm.openai_llm import OpenAILLM
from app.documents.processor import DocumentProcessor
from app.graph.workflow import build_graph


def main():
    print("🚀 Starting native test run")

    # Initialize LLM provider
    llm_provider = OpenAILLM()

    # Document processor
    processor = DocumentProcessor(
        embeddings=llm_provider.embeddings()
    )

    # Build LangGraph
    graph = build_graph(
        processor,
        llm_provider.chat()
    )

    # ---- TEST 1: Upload / ingest document ----
    content = """
    Machine Learning is a field of AI.
    Types include supervised, unsupervised, and reinforcement learning.
    """

    chunks = processor.ingest(
        content=content,
        source="ml_intro.txt"
    )

    print(f"Document ingested into {chunks} chunks")

    # ---- TEST 2: QA ----
    result = graph.invoke({
        "query": "What are the types of machine learning?",
        "agent_type": "qa"
    })

    print("\nQA RESULT:")
    print(result["result"])

    # ---- TEST 3: Learning material ----
    result = graph.invoke({
        "query": "what is supervised learning? explain in detail",
        "agent_type": "learning"
    })

    print("\n📘 LEARNING MATERIAL (preview):")
    print(result["result"][:500])

    # ---- TEST 4: Quiz ----
    result = graph.invoke({
        "query": "machine learning",
        "agent_type": "quiz"
    })

    print("\nQUIZ:")
    print(result["result"])

if __name__ == "__main__":
    main()
