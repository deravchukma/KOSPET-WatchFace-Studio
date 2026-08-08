from pathlib import Path

from kospet_watchface_studio.explorer.models import (
    ManifestInfo,
    ManifestPlatform,
    ManifestVersion,
    WatchfaceAsset,
    WatchfacePackageInfo,
)


def test_package() -> None:
    manifest = ManifestInfo(
        id=1,
        name="Demo",
        app_type="watchface",
        version=ManifestVersion(
            code=1,
            name="1.0.0",
        ),
        design_width=454,
        platforms=(
            ManifestPlatform(
                name="Amazfit T-Rex 2",
                device_source=418,
            ),
        ),
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
        size=600,
    )

    assert package.asset_count == 3
    assert package.image_count == 2
    assert package.size == 600