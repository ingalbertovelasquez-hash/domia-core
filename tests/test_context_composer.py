from domia.cognition.context_composer.context_composer import ContextComposer
from domia.cognition.contracts.intent import Intent
from domia.cognition.decision_engine.decision import Decision
from domia.cognition.planner.plan import Plan


def test_context_composer():

    composer = ContextComposer()

    intent = Intent(
        action="create",
        domain="education",
        subject="Curso IA",
        confidence=0.95,
        required_capabilities=[],
    )

    plan = Plan(
        objective="Curso IA",
        steps=[
            "Analyze Intent",
            "Search Knowledge",
            "Build Context",
        ],
    )

    decision = Decision(
        objective="Curso IA",
        recommended_nodes=[
            "DomIA",
            "Kairos GPT",
        ],
        reasoning="Knowledge ranked by keyword relevance.",
    )

    context = composer.compose(
        objective="Curso IA",
        intent=intent,
        plan=plan,
        decision=decision,
    )

    assert context.objective == "Curso IA"
    assert context.intent == "create"

    assert len(context.plan) == 3

    assert context.knowledge == [
        "DomIA",
        "Kairos GPT",
    ]

    assert context.notes == [
        "Domain: education",
        "Confidence: 0.95",
    ]