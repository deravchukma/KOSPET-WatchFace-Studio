"""
Manifest model.

Represents metadata extracted from app.json.
"""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class ManifestVersion:
    """Watchface package version."""

    code: int
    name: str


@dataclass(slots=True, frozen=True)
class ManifestPlatform:
    """Target platform supported by the watchface."""

    name: str
    device_source: int

@dataclass(slots=True, frozen=True)
class ManifestInfo:
    """Metadata extracted from a Zepp app.json manifest."""

    id: int
    name: str
    app_type: str
    version: ManifestVersion
    design_width: int
    platforms: tuple[ManifestPlatform, ...]

    @property
    def version_name(self) -> str:
        """Return human-readable version."""
        return self.version.name

    @property
    def version_code(self) -> int:
        """Return numeric version code."""
        return self.version.code

    @property
    def resolution(self) -> tuple[int, int]:
        """
        Return design resolution.

        Zepp's manifest provides designWidth. For the current
        watchface format, the design canvas is square.
        """
        return (self.design_width, self.design_width)

    @property
    def width(self) -> int:
        """Return design width."""
        return self.design_width

    @property
    def height(self) -> int:
        """Return design height."""
        return self.design_width

    @property
    def is_square(self) -> bool:
        """Return True if the design canvas is square."""
        return True