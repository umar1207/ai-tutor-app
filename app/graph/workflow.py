from langgraph.graph import StateGraph, END
from app.agents.qa import QAAgent
from app.agents.quiz import QuizAgent
from app.agents.learning import LearningAgent
from app.agents.rag import RAGAgent


def build_graph(document_processor, llm):
    rag_agent = RAGAgent(document_processor)
    qa = QAAgent(llm)
    quiz = QuizAgent(llm)
    learning = LearningAgent(llm)

    graph = StateGraph(dict)

    graph.add_node("retrieve", rag_agent.retrieve)

    # graph.add_node("retrieve", lambda s: {
    #     **s,
    #     "retrieved_docs": retriever.get_relevant_documents(s["query"])
    # })

    graph.add_node("qa", lambda s: {**s, "result": qa.run(s["query"], s["retrieved_docs"])})
    graph.add_node("quiz", lambda s: {**s, "result": quiz.run(s["query"], s["retrieved_docs"])})
    graph.add_node("learning", lambda s: {**s, "result": learning.run(s["query"], s["retrieved_docs"])})

    graph.set_entry_point("retrieve")

    graph.add_conditional_edges(
        "retrieve",
        lambda s: s["agent_type"],
        {"qa": "qa", "quiz": "quiz", "learning": "learning"}
    )

    graph.add_edge("qa", END)
    graph.add_edge("quiz", END)
    graph.add_edge("learning", END)

    return graph.compile()
