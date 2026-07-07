from domia.inference.openai_provider import OpenAIProvider


def test_openai_provider_creation():

    provider = OpenAIProvider()

    assert provider.model == "gpt-5.5"