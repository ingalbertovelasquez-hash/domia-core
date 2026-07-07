import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Configuración centralizada de DomIA.
    """

    provider: str = "mock"

    model: str = "gpt-5.5"

    api_key: str | None = None

    @classmethod
    def load(cls) -> "Settings":

        return cls(
            provider=os.getenv(
                "DOMIA_PROVIDER",
                "mock",
            ),
            model=os.getenv(
                "DOMIA_MODEL",
                "gpt-5.5",
            ),
            api_key=os.getenv(
                "OPENAI_API_KEY",
            ),
        )