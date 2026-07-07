from domia.inference.provider import Provider


class MockProvider(Provider):
    """
    Proveedor simulado utilizado para pruebas.
    """

    def generate(self, prompt: str) -> str:

        return (
            "Mock Response\n\n"
            f"Prompt received:\n{prompt}"
        )