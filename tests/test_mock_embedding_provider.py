from domia.embeddings.mock_embedding_provider import (
    MockEmbeddingProvider,
)


def test_mock_embedding_provider():

    provider = MockEmbeddingProvider()

    vector = provider.embed(
        "DomIA"
    )

    assert isinstance(vector, list)

    assert len(vector) == 8

    assert all(
        isinstance(value, float)
        for value in vector
    )