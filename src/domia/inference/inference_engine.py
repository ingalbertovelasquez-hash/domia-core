from domia.inference.provider import Provider


class InferenceEngine:
    """
    Motor de inferencia.

    Delega la generación de respuestas
    al proveedor configurado.
    """

    def __init__(self, provider: Provider):

        self.provider = provider

    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)