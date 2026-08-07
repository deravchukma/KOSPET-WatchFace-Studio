from kospet_watchface_studio.explorer.parser import ManifestParser


DM_APP_JSON = """
{
    "configVersion": "v2",
    "app": {
        "appIdType": 0,
        "appId": 1017455,
        "appName": "DM",
        "appType": "watchface",
        "version": {
            "code": 3,
            "name": "1.0.2"
        },
        "vender": "zepp",
        "description": "",
        "icon": "1.png",
        "cover": ["1.png"]
    },
    "platforms": [
        {
            "name": "Amazfit GTR 3",
            "deviceSource": 226
        },
        {
            "name": "Amazfit T-Rex 2",
            "deviceSource": 418
        },
        {
            "name": "Amazfit T-Rex 2",
            "deviceSource": 419
        }
    ],
    "designWidth": 454
}
"""


def test_parse_dm_manifest() -> None:
    parser = ManifestParser()

    manifest = parser.parse(DM_APP_JSON)

    assert manifest.id == 1017455
    assert manifest.name == "DM"
    assert manifest.app_type == "watchface"

    assert manifest.version_name == "1.0.2"
    assert manifest.version_code == 3

    assert manifest.width == 454
    assert manifest.height == 454
    assert manifest.resolution == (454, 454)

    assert len(manifest.platforms) == 3

    assert manifest.platforms[0].name == "Amazfit GTR 3"
    assert manifest.platforms[1].name == "Amazfit T-Rex 2"
    assert manifest.platforms[1].device_source == 418