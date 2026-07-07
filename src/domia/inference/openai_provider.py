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

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = model

    def generate(self, prompt: str) -> str:

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text