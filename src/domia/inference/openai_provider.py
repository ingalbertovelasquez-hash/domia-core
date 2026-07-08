import os

from openai import OpenAI

from domia.inference.provider import Provider


class OpenAIProvider(Provider):
    """
    Proveedor oficial de OpenAI.

    Implementa el contrato Provider para generar
    respuestas utilizando la API de OpenAI.
    """

    def __init__(
        self,
        model: str = "gpt-5.5",
    ) -> None:

        self.model = model

        self._client: OpenAI | None = None

    @property
    def client(self) -> OpenAI:
        """
        Crea el cliente únicamente cuando
        realmente se necesita.
        """

        if self._client is None:

            self._client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )

        return self._client

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text