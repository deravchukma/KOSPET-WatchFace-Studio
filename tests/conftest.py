from pathlib import Path

import pytest


@pytest.fixture
def dm_watchface() -> Path:
    return Path("tests/data/DM_1017455.zip")