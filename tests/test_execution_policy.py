from domia.cognition.contracts.intent import Intent
from domia.cognition.execution_policy.execution_policy import ExecutionPolicy


def test_create_execution_policy():

    policy_engine = ExecutionPolicy()

    intent = Intent(
        action="create",
        domain="education",
        subject="Curso IA",
        confidence=0.95,
        required_capabilities=[
            "knowledge_search",
            "context_builder",
        ],
    )

    policy = policy_engine.create(intent)

    assert policy.use_memory is True

    assert policy.use_knowledge_graph is True

    assert policy.build_context is True

    assert policy.build_prompt is True

    assert policy.execute_model is False

    assert len(policy.capabilities) == 2