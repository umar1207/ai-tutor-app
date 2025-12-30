from langchain_openai import OpenAIEmbeddings
from app.config.settings import Settings

def get_embeddings():
    return OpenAIEmbeddings(
        model=Settings.EMBEDDING_MODEL,
        api_key=Settings.OPENAI_API_KEY,
        base_url=Settings.OPENAI_BASE_URL
    )
