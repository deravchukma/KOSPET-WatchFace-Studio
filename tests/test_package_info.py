from pathlib import Path

from kospet_watchface_studio.explorer.models import (
    ManifestInfo,
    WatchfaceAsset,
    WatchfacePackageInfo,
)


def test_package():
    manifest = ManifestInfo(
        id=1,
        name="Demo",
        version="1.0.0",
        resolution=(454, 454),
    )

    assets = (
        WatchfaceAsset(Path("a.png"), 100),
        WatchfaceAsset(Path("b.png"), 200),
        WatchfaceAsset(Path("app.js"), 300),
    )

    package = WatchfacePackageInfo(
        path=Path("demo.zip"),
        manifest=manifest,
        assets=assets,
        app_json=Path("app.json"),
        app_js=Path("app.js"),
    )

    assert package.asset_count == 3
    assert package.image_count == 2
    assert package.total_size == 600