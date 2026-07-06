from domia.cognition.contracts.context import Context
from domia.cognition.prompt_builder.prompt_builder import PromptBuilder


def test_prompt_builder():

    builder = PromptBuilder()

    context = Context(
        objective="Create an AI course",
        intent="create",
        plan=[
            "Analyze Intent",
            "Search Knowledge",
            "Build Context",
        ],
        knowledge=[
            "DomIA",
            "Kairos GPT",
        ],
        notes=[
            "Domain: education",
            "Confidence: 0.95",
        ],
    )

    prompt = builder.build(context)

    assert "Objective: Create an AI course" in prompt
    assert "Intent: create" in prompt

    assert "- Analyze Intent" in prompt
    assert "- Search Knowledge" in prompt
    assert "- Build Context" in prompt

    assert "- DomIA" in prompt
    assert "- Kairos GPT" in prompt

    assert "- Domain: education" in prompt
    assert "- Confidence: 0.95" in prompt

    assert "Generate the best possible response." in prompt