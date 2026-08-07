"""
Asset model.

Represents a single resource contained in a watchface package.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class WatchfaceAsset:
    """
    A single file contained in a watchface package.
    """

    path: Path
    size: int

    @property
    def name(self) -> str:
        """Return file name."""
        return self.path.name

    @property
    def extension(self) -> str:
        """Return lower-case extension."""
        return self.path.suffix.lower()

    @property
    def stem(self) -> str:
        """Return filename without extension."""
        return self.path.stem

    @property
    def is_image(self) -> bool:
        """True if the asset is an image."""
        return self.extension in {
            ".png",
            ".jpg",
            ".jpeg",
            ".bmp",
            ".gif",
            ".webp",
        }