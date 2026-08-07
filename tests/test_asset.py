from pathlib import Path

from kospet_watchface_studio.explorer.models.asset import WatchfaceAsset


def test_asset_properties():
    asset = WatchfaceAsset(
        path=Path("assets/background.png"),
        size=12345,
    )

    assert asset.name == "background.png"
    assert asset.stem == "background"
    assert asset.extension == ".png"
    assert asset.is_image


def test_non_image_asset():
    asset = WatchfaceAsset(
        path=Path("app.js"),
        size=100,
    )

    assert not asset.is_image