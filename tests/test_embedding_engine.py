from domia.embeddings.embedding_engine import (
    EmbeddingEngine,
)
from domia.embeddings.mock_embedding_provider import (
    MockEmbeddingProvider,
)


def test_embedding_engine():

    provider = MockEmbeddingProvider()

    engine = EmbeddingEngine(provider)

    vector = engine.embed(
        "Artificial Intelligence"
    )

    assert len(vector) == 8

    assert isinstance(vector, list)