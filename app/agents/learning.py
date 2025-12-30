from langchain_core.prompts import ChatPromptTemplate


class LearningAgent:

    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Prepare a detailed learning material based on the context received."),
            ("human", "Context:\n{context}\n\nQuestion:\n{question}")
        ])

    def run(self, query, docs):
        context = "\n\n".join(d.page_content for d in docs)
        chain = self.prompt | self.llm
        return chain.invoke({"context": context, "question": query}).content
