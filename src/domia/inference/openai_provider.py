from openai import OpenAI

from domia.config.settings import Settings
from domia.inference.provider import Provider


class OpenAIProvider(Provider):
    """
    Proveedor oficial de OpenAI.

    Implementa el contrato Provider para generar
    respuestas utilizando la API de OpenAI.
    """

    def __init__(
        self,
        model: str | None = None,
    ) -> None:

        settings = Settings.load()

        self.model = model or settings.model

        self.client = OpenAI(
            api_key=settings.api_key,
        )

    def generate(self, prompt: str) -> str:

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text