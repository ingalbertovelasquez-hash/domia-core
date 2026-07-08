from domia.embeddings.embedding_engine import EmbeddingEngine
from domia.vectorstore.vector_document import VectorDocument
from domia.vectorstore.vector_store import VectorStore


class SemanticRetriever:
    """
    Recuperador semántico.

    Convierte una consulta en un embedding
    y realiza una búsqueda de similitud
    sobre el Vector Store.
    """

    def __init__(
        self,
        embedding_engine: EmbeddingEngine,
        vector_store: VectorStore,
    ) -> None:

        self.embedding_engine = embedding_engine
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[VectorDocument]:
        """
        Recupera los documentos más similares
        a la consulta.
        """

        embedding = self.embedding_engine.embed(
            query
        )

        return self.vector_store.similarity_search(
            embedding=embedding,
            top_k=top_k,
        )