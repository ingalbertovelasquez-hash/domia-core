from domia.bootstrap.foundation import load_foundation_graph
from domia.cognition.decision_engine.decision_engine import DecisionEngine


def test_decision_engine():

    graph = load_foundation_graph()

    engine = DecisionEngine(graph)

    decision = engine.decide(
        "DomIA PECRA"
    )

    assert decision.objective == "DomIA PECRA"

    assert len(decision.recommended_nodes) >= 2

    assert "DomIA" in decision.recommended_nodes

    assert "PECRA" in decision.recommended_nodes