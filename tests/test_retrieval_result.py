from domia.retrieval.retrieval_result import RetrievalResult
from domia.vectorstore.vector_document import VectorDocument


def test_retrieval_result():

    document = VectorDocument(
        id="1",
        text="Artificial Intelligence",
        embedding=[1.0] * 8,
    )

    result = RetrievalResult(
        document=document,
        score=0.95,
    )

    assert result.document.text == "Artificial Intelligence"

    assert result.score == 0.95