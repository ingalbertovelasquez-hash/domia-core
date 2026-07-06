from domia.cognition.contracts.intent import Intent


def test_create_intent():

    intent = Intent(
        action="create",
        domain="education",
        subject="AI course",
        confidence=0.95,
        required_capabilities=[
            "knowledge_search",
            "context_builder",
        ],
    )

    assert intent.action == "create"

    assert intent.domain == "education"

    assert intent.subject == "AI course"

    assert intent.confidence == 0.95

    assert len(intent.required_capabilities) == 2