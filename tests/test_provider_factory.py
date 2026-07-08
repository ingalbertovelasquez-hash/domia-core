import pytest

from domia.inference.mock_provider import MockProvider
from domia.inference.ollama_provider import OllamaProvider
from domia.inference.openai_provider import OpenAIProvider
from domia.inference.provider_factory import ProviderFactory


def test_create_mock_provider():

    provider = ProviderFactory.create("mock")

    assert isinstance(provider, MockProvider)


def test_create_openai_provider():

    provider = ProviderFactory.create("openai")

    assert isinstance(provider, OpenAIProvider)


def test_create_ollama_provider():

    provider = ProviderFactory.create("ollama")

    assert isinstance(provider, OllamaProvider)


def test_unknown_provider():

    with pytest.raises(ValueError):

        ProviderFactory.create("unknown")