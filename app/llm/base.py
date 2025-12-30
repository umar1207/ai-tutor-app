from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def chat(self):
        pass

    @abstractmethod
    def embeddings(self):
        pass
