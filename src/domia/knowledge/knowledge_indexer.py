from domia.domain.services.knowledge_graph import KnowledgeGraph
from domia.embeddings.embedding_engine import EmbeddingEngine
from domia.vectorstore.vector_document import VectorDocument
from domia.vectorstore.vector_store import VectorStore


class KnowledgeIndexer:
    """
    Construye un índice vectorial a partir
    del Knowledge Graph.

    Cada nodo se transforma en un documento
    vectorial utilizando el Embedding Engine.
    """

    def __init__(
        self,
        graph: KnowledgeGraph,
        embedding_engine: EmbeddingEngine,
        vector_store: VectorStore,
    ) -> None:

        self.graph = graph
        self.embedding_engine = embedding_engine
        self.vector_store = vector_store

    def build(self) -> None:
        """
        Recorre todos los nodos del grafo
        y los indexa en el Vector Store.
        """

        for node in self.graph.all_nodes():

            text = (
                f"{node.name}\n"
                f"{node.node_type}\n"
                f"{node.description}"
            )

            embedding = self.embedding_engine.embed(
                text
            )

            self.vector_store.add(
                VectorDocument(
                    id=node.id,
                    text=node.name,
                    embedding=embedding,
                )
            )