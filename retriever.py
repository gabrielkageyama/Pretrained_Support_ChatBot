##Solution found online
# since the program got stuck with
# package compatibility problems

from typing import List
from langchain.schema import BaseRetriever, Document
from langchain.vectorstores.base import VectorStoreRetriever


class CompatibleRetriever(BaseRetriever):
    """A wrapper to make VectorStoreRetriever compatible with BaseRetriever."""

    def __init__(self, vectorstore_retriever: VectorStoreRetriever):
        self.vectorstore_retriever = vectorstore_retriever

    def get_relevant_documents(self, query: str) -> List[Document]:
        """Synchronously retrieve relevant documents."""
        return self.vectorstore_retriever.get_relevant_documents(query)

    async def aget_relevant_documents(self, query: str) -> List[Document]:
        """Asynchronously retrieve relevant documents."""
        import asyncio
        return await asyncio.to_thread(self.vectorstore_retriever.get_relevant_documents, query)


def get_compatible_retriever(vectorstore, **kwargs) -> BaseRetriever:
    """Utility to create a CompatibleRetriever."""
    vectorstore_retriever = VectorStoreRetriever(vectorstore=vectorstore, **kwargs)
    return CompatibleRetriever(vectorstore_retriever)
