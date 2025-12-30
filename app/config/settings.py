import os
from dotenv import load_dotenv
from pathlib import Path

HOME = Path.home()

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

    CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    CHROMA_DIR = HOME / "tutor-mcp" / "chroma"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
