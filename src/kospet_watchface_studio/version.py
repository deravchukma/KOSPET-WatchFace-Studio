"""
Version information for KOSPET WatchFace Studio.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True, slots=True, order=True)
class VersionInfo:
    """Semantic version information."""

    major: int
    minor: int
    patch: int

    @property
    def text(self) -> str:
        """Return version as a string."""
        return f"{self.major}.{self.minor}.{self.patch}"


VERSION: Final = VersionInfo(
    major=0,
    minor=1,
    patch=0,
)

__version__: Final[str] = "0.1.0"

__title__: Final[str] = "KOSPET WatchFace Studio"
__package__: Final[str] = "kospet_watchface_studio"

__author__: Final[str] = "KOSPET WatchFace Studio Contributors"

__license__: Final[str] = "MIT"

__repository__: Final[str] = (
    "https://github.com/deravchukma/KOSPET-WatchFace-Studio"
)