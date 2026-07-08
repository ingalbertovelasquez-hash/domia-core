from domia.bootstrap.foundation import load_foundation_graph
from domia.retrieval.keyword_retriever import KeywordRetriever


def test_keyword_retriever():

    graph = load_foundation_graph()

    retriever = KeywordRetriever(graph)

    results = retriever.retrieve(
        "DomIA PECRA",
        top_k=5,
    )

    assert len(results) >= 2

    texts = [
        result.document.text
        for result in results
    ]

    assert "DomIA" in texts

    assert "PECRA" in texts


def test_keyword_retriever_top_k():

    graph = load_foundation_graph()

    retriever = KeywordRetriever(graph)

    results = retriever.retrieve(
        "Artificial Intelligence Machine Learning",
        top_k=2,
    )

    assert len(results) <= 2