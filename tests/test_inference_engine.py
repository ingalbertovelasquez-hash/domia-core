from domia.inference.inference_engine import InferenceEngine
from domia.inference.mock_provider import MockProvider


def test_inference_engine():

    engine = InferenceEngine(MockProvider())

    response = engine.generate(
        "Create an AI course"
    )

    assert "Mock Response" in response

    assert "Create an AI course" in response