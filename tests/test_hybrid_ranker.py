from domia.retrieval.hybrid_ranker import HybridRanker


def test_hybrid_ranker_default():

    ranker = HybridRanker()

    score = ranker.score(
        keyword_score=1.0,
        semantic_score=0.8,
    )

    assert score == 0.9


def test_hybrid_ranker_custom_weights():

    ranker = HybridRanker(
        keyword_weight=0.7,
        semantic_weight=0.3,
    )

    score = ranker.score(
        keyword_score=1.0,
        semantic_score=0.5,
    )

    assert score == 0.85