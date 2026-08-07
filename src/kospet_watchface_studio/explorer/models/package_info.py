#@dataclass(slots=True, frozen=True)
#class WatchfacePackageInfo:
#    path: Path
#    name: str
#    version: str | None
#    package_type: str
"""
Watchface package information model.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
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
    #app_json: Path
    #app_js: Path
    size: int

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
    
@cached_property
def asset_index(self) -> dict[str, WatchfaceAsset]:
    """Return assets indexed by archive path."""
    return {
        asset.path.as_posix(): asset
        for asset in self.assets
    }