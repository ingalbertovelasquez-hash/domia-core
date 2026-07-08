from domia.bootstrap.foundation import load_foundation_graph
from domia.embeddings.embedding_engine import EmbeddingEngine
from domia.embeddings.mock_embedding_provider import (
    MockEmbeddingProvider,
)
from domia.knowledge.knowledge_indexer import (
    KnowledgeIndexer,
)
from domia.vectorstore.vector_store import VectorStore


def test_knowledge_indexer():

    graph = load_foundation_graph()

    vector_store = VectorStore()

    embedding_engine = EmbeddingEngine(
        MockEmbeddingProvider()
    )

    indexer = KnowledgeIndexer(
        graph=graph,
        embedding_engine=embedding_engine,
        vector_store=vector_store,
    )

    indexer.build()

    assert (
        vector_store.count()
        == graph.node_count()
    )