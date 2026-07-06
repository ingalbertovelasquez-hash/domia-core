from domia.domain.entities.cognitive_asset import CognitiveAsset


def test_create_asset():
    asset = CognitiveAsset(
        name="DomIA",
        asset_type="Project"
    )

    assert asset.name == "DomIA"
    assert asset.asset_type == "Project"
    assert asset.status == "active"