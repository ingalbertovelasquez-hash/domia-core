from domia.cognition.contracts.intent import Intent
from domia.cognition.planner.planner import Planner


def test_create_plan():

    planner = Planner()

    intent = Intent(
        action="create",
        domain="education",
        subject="Curso de IA",
        confidence=0.95,
        required_capabilities=[
            "knowledge_search",
            "context_builder",
        ],
    )

    plan = planner.create_plan(intent)

    assert plan.objective == "Curso de IA"

    assert len(plan.steps) == 6

    assert plan.steps[0] == "Analyze Intent"

    assert plan.steps[-1] == "Validate Response"