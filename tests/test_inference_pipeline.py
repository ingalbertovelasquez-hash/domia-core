from domia.application.pipelines.inference_pipeline import (
    InferencePipeline,
)
from domia.cognition.contracts.context import Context


def test_inference_pipeline():

    pipeline = InferencePipeline()

    context = Context(
        objective="Crear un curso de IA",
        intent="create",
        plan=["Analizar", "Planificar"],
        knowledge=["AI Fundamentals"],
        notes=["Dominio: Educación"],
    )

    result = pipeline.run(context)

    assert result["status"] == "COMPLETED"

    assert "Objective:" in result["prompt"]

    assert isinstance(result["response"], str)

    assert len(result["response"]) > 0