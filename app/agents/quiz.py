from langchain_core.prompts import ChatPromptTemplate


class QuizAgent:

    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Prepare a quiz based on the context."),
            ("human", "Context:\n{context}\n\nQuestion:\n{question}")
        ])

    def run(self, query, docs):
        context = "\n\n".join(d.page_content for d in docs)
        chain = self.prompt | self.llm
        return chain.invoke({"context": context, "question": query}).content
