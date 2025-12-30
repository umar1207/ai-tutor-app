from langchain_chroma import Chroma
from app.config.settings import Settings
from pathlib import Path
import sys


def load_vectorstore(embeddings):
    path = Path(Settings.CHROMA_DIR)

    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"[FATAL] Cannot create Chroma directory: {path}", file=sys.stderr)
        raise

    return Chroma(
        persist_directory=str(path),
        embedding_function=embeddings,
        collection_name="documents"
    )
