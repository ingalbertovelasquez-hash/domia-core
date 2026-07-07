from domia.application.pipelines.ask_pipeline import AskPipeline


def test_run_pipeline():

    pipeline = AskPipeline()

    result = pipeline.run(
        "Quiero crear un curso de IA para abogados"
    )

    assert result["status"] == "COMPLETED"

    assert result["intent"].action == "create"

    assert result["decision"] is not None

    assert result["context"] is not None

    assert result["prompt"] is not None

    assert result["response"] is not None

    assert "Objective:" in result["prompt"]