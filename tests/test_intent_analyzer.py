from domia.cognition.intent_analyzer.intent_analyzer import IntentAnalyzer
from domia.cognition.contracts.objective import Objective


def test_analyze_create_course():

    analyzer = IntentAnalyzer()

    objective = Objective(
        text="Quiero diseñar un curso de IA para abogados"
    )

    intent = analyzer.analyze(objective)

    assert intent.action == "create"

    assert intent.domain == "education"

    assert "curso" in intent.subject.lower()

    assert intent.confidence >= 0.90

    assert "knowledge_search" in intent.required_capabilities