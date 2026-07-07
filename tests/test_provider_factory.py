from domia.inference.mock_provider import MockProvider
from domia.inference.provider_factory import ProviderFactory


def test_provider_factory():

    provider = ProviderFactory.create("mock")

    assert isinstance(provider, MockProvider)