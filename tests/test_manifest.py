from kospet_watchface_studio.explorer.models.manifest import ManifestInfo


def test_manifest():
    manifest = ManifestInfo(
        id=1017455,
        name="DM",
        version="1.0.2",
        resolution=(454, 454),
    )

    assert manifest.width == 454
    assert manifest.height == 454
    assert manifest.is_square


def test_rectangular_manifest():
    manifest = ManifestInfo(
        id=None,
        name="Demo",
        version=None,
        resolution=(466, 466),
    )

    assert manifest.width == 466
    assert manifest.height == 466