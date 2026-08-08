from kospet_watchface_studio.explorer.models import (
    ManifestInfo,
    ManifestPlatform,
    ManifestVersion,
)


def test_manifest() -> None:
    manifest = ManifestInfo(
        id=1017455,
        name="DM",
        app_type="watchface",
        version=ManifestVersion(
            code=3,
            name="1.0.2",
        ),
        design_width=454,
        platforms=(
            ManifestPlatform(
                name="Amazfit T-Rex 2",
                device_source=418,
            ),
        ),
    )

    assert manifest.id == 1017455
    assert manifest.name == "DM"
    assert manifest.app_type == "watchface"

    assert manifest.version_name == "1.0.2"
    assert manifest.version_code == 3

    assert manifest.width == 454
    assert manifest.height == 454
    assert manifest.resolution == (454, 454)

    assert manifest.is_square


def test_different_design_width() -> None:
    manifest = ManifestInfo(
        id=2,
        name="Demo",
        app_type="watchface",
        version=ManifestVersion(
            code=1,
            name="1.0.0",
        ),
        design_width=466,
        platforms=(),
    )

    assert manifest.width == 466
    assert manifest.height == 466
    assert manifest.resolution == (466, 466)
    assert manifest.is_square