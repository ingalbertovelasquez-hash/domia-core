from domia.embeddings.embedding_engine import EmbeddingEngine
from domia.embeddings.mock_embedding_provider import (
    MockEmbeddingProvider,
)
from domia.retrieval.semantic_retriever import (
    SemanticRetriever,
)
from domia.vectorstore.vector_document import (
    VectorDocument,
)
from domia.vectorstore.vector_store import VectorStore


def test_semantic_retriever():

    embedding_engine = EmbeddingEngine(
        MockEmbeddingProvider()
    )

    vector_store = VectorStore()

    ai_embedding = embedding_engine.embed(
        "Artificial Intelligence"
    )

    ml_embedding = embedding_engine.embed(
        "Machine Learning"
    )

    vector_store.add(
        VectorDocument(
            id="1",
            text="Artificial Intelligence",
            embedding=ai_embedding,
        )
    )

    vector_store.add(
        VectorDocument(
            id="2",
            text="Machine Learning",
            embedding=ml_embedding,
        )
    )

    retriever = SemanticRetriever(
        embedding_engine=embedding_engine,
        vector_store=vector_store,
    )

    results = retriever.retrieve(
        "Artificial Intelligence",
        top_k=1,
    )

    assert len(results) == 1

    assert (
        results[0].text
        == "Artificial Intelligence"
    )