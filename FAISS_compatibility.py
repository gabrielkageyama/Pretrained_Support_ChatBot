from langchain.vectorstores import VectorStore
from langchain_community.vectorstores import FAISS


class CompatibleFAISS(FAISS, VectorStore):
    # Ensures FAISS inherits from VectorStore for compatibility.
    pass
