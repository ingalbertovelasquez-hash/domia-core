from domia.application.pipelines.ask_pipeline import AskPipeline


def test_run_pipeline():

    pipeline = AskPipeline()

    result = pipeline.run(
        "Quiero crear un curso de IA para abogados"
    )

    assert result["status"] == "READY"

    assert result["intent"].action == "create"

    assert len(result["plan"].steps) == 6

    assert result["decision"] is not None