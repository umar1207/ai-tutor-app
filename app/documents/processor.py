from datetime import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.config.settings import Settings
from app.documents.vectorstore import load_vectorstore


class DocumentProcessor:

    def __init__(self, embeddings):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=Settings.CHUNK_SIZE,
            chunk_overlap=Settings.CHUNK_OVERLAP
        )
        self.vs = load_vectorstore(embeddings=embeddings)

    def ingest(self, content: str, source: str):
        doc = Document(
            page_content=content,
            metadata={
                "source": source,
                "uploaded_at": str(datetime.now())
            }
        )

        chunks = self.splitter.split_documents([doc])
        self.vs.add_documents(chunks)
        return len(chunks)

    def retriever(self, k=4):
        return self.vs.as_retriever(search_kwargs={"k": k})
