from domia.config.settings import Settings


def test_default_settings():

    settings = Settings.load()

    assert settings.provider in (
        "mock",
        "openai",
        "ollama",
    )

    assert settings.model