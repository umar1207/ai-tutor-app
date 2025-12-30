from langchain_core.prompts import ChatPromptTemplate


class QAAgent:

    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer only using provided context."),
            ("human", "Context:\n{context}\n\nQuestion:\n{question}")
        ])

    def run(self, query, docs):
        context = "\n\n".join(d.page_content for d in docs)
        chain = self.prompt | self.llm
        return chain.invoke({"context": context, "question": query}).content
