from pathlib import Path

from kospet_watchface_studio.utils.filesystem import (
    human_size,
    is_supported_package,
)


def test_human_size():
    assert human_size(0) == "0 B"
    assert human_size(512) == "512 B"
    assert human_size(1024) == "1.0 KB"
    assert human_size(1536) == "1.5 KB"
    assert human_size(1024 * 1024) == "1.0 MB"


def test_supported_extensions():
    assert is_supported_package(Path("demo.zip"))
    assert is_supported_package(Path("demo.bin"))

    assert not is_supported_package(Path("demo.txt"))
    assert not is_supported_package(Path("demo.png"))