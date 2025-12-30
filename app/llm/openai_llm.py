from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.config.settings import Settings
from app.llm.base import BaseLLM


class OpenAILLM(BaseLLM):

    def chat(self):
        return ChatOpenAI(
            model=Settings.CHAT_MODEL,
            api_key=Settings.OPENAI_API_KEY,
            base_url=Settings.OPENAI_BASE_URL,
            temperature=0.7
        )

    def embeddings(self):
        return OpenAIEmbeddings(
            model=Settings.EMBEDDING_MODEL,
            api_key=Settings.OPENAI_API_KEY,
            base_url=Settings.OPENAI_BASE_URL
        )