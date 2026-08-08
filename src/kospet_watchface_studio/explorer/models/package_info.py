"""
Watchface package information model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .asset import WatchfaceAsset
from .manifest import ManifestInfo


@dataclass(slots=True, frozen=True)
class WatchfacePackageInfo:
    """
    Basic information about a watchface package.
    """

    path: Path
    manifest: ManifestInfo | None
    assets: tuple[WatchfaceAsset, ...]
    size: int
    _asset_index: dict[str, WatchfaceAsset] | None = field(
        default=None, init=False, repr=False, compare=False
    )

    @property
    def asset_count(self) -> int:
        """Return number of assets."""
        return len(self.assets)

    @property
    def image_count(self) -> int:
        """Return number of image assets."""
        return sum(asset.is_image for asset in self.assets)

    @property
    def total_size(self) -> int:
        return sum(asset.size for asset in self.assets)
    
    @property
    def asset_index(self) -> dict[str, WatchfaceAsset]:
        """
        Return assets indexed by archive path.

        Computed lazily on first access and cached. Uses a dedicated
        slot instead of functools.cached_property, because
        cached_property requires an instance __dict__, which
        slots=True removes.
        """
        if self._asset_index is None:
            object.__setattr__(
                self,
                "_asset_index",
                {asset.path.as_posix(): asset for asset in self.assets},
            )
        return self._asset_index