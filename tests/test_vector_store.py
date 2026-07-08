from domia.vectorstore.vector_document import VectorDocument
from domia.vectorstore.vector_store import VectorStore


def test_vector_store():

    store = VectorStore()

    store.add(
        VectorDocument(
            id="1",
            text="Artificial Intelligence",
            embedding=[
                1.0,
                1.0,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
            ],
        )
    )

    store.add(
        VectorDocument(
            id="2",
            text="Machine Learning",
            embedding=[
                0.9,
                0.9,
                0.9,
                0.9,
                0.0,
                0.0,
                0.0,
                0.0,
            ],
        )
    )

    store.add(
        VectorDocument(
            id="3",
            text="Cooking",
            embedding=[
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
            ],
        )
    )

    results = store.similarity_search(
        [
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        top_k=2,
    )

    assert store.count() == 3

    assert len(results) == 2

    texts = {doc.text for doc in results}

    assert "Artificial Intelligence" in texts

    assert "Machine Learning" in texts

    assert "Cooking" not in texts