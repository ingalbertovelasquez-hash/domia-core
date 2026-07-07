from domia.cognition.contracts.context import Context
from domia.cognition.prompt_builder.prompt_builder import PromptBuilder
from domia.inference.inference_engine import InferenceEngine
from domia.inference.provider_factory import ProviderFactory


class InferencePipeline:
    """
    Pipeline encargado de transformar un contexto
    cognitivo en una respuesta utilizando
    la capa de inferencia.
    """

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        provider = ProviderFactory.create()

        self.engine = InferenceEngine(
            provider
        )

    def run(self, context: Context) -> dict:

        prompt = self.prompt_builder.build(context)

        response = self.engine.generate(prompt)

        return {
            "prompt": prompt,
            "response": response,
            "status": "COMPLETED",
        }