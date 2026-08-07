from pathlib import Path

from kospet_watchface_studio.explorer.loader import WatchfaceLoader


def test_loader_load(dm_watchface: Path) -> None:
    loader = WatchfaceLoader()

    package = loader.load(dm_watchface)

    assert package.asset_count == 177
    assert package.image_count == 175
    assert package.size > 0

    assert package.manifest is not None

    assert package.manifest.id == 1017455
    assert package.manifest.name == "DM"
    assert package.manifest.app_type == "watchface"

    assert package.manifest.version_name == "1.0.2"
    assert package.manifest.version_code == 3

    assert package.manifest.resolution == (454, 454)