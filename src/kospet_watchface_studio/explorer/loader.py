"""
Watchface package loader.

Loads watchface packages directly from ZIP archives without extracting
them to disk.
"""

from __future__ import annotations

from pathlib import Path
from zipfile import BadZipFile, ZipFile

from kospet_watchface_studio.constants import (
    SUPPORTED_ARCHIVE_EXTENSIONS,
    ZEPP_APP_JSON,
)
from kospet_watchface_studio.exceptions import (
    InvalidPackageError,
    UnsupportedPackageError,
)
from kospet_watchface_studio.utils.filesystem import (
    ensure_exists,
    file_size,
)

from .models import WatchfaceAsset, WatchfacePackageInfo
from .parser import ManifestParser


class WatchfaceLoader:
    """Load watchface packages."""

    def __init__(self, parser: ManifestParser | None = None) -> None:
        """
        Initialize the loader.

        Parameters
        ----------
        parser:
            Optional manifest parser instance.
        """
        self._parser = parser or ManifestParser()

    def load(self, path: Path) -> WatchfacePackageInfo:
        """
        Load a watchface package from a ZIP archive.

        The archive is never extracted to disk. ``app.json`` is read
        directly from the ZIP and passed to ``ManifestParser``.
        """
        ensure_exists(path)

        if not path.is_file():
            raise InvalidPackageError(
                f"Package path is not a file: {path}"
            )

        if path.suffix.lower() not in SUPPORTED_ARCHIVE_EXTENSIONS:
            raise UnsupportedPackageError(path)

        try:
            with ZipFile(path) as archive:
                assets = self._build_assets(archive)
                manifest = self._parse_manifest(archive)

        except BadZipFile as exc:
            raise InvalidPackageError(
                f"Invalid ZIP archive: {path}"
            ) from exc

        return WatchfacePackageInfo(
            path=path,
            manifest=manifest,
            assets=assets,
            size=file_size(path),
        )

    @staticmethod
    def _build_assets(archive: ZipFile) -> tuple[WatchfaceAsset, ...]:
        """Build asset models from ZIP archive entries."""
        return tuple(
            WatchfaceAsset(
                path=Path(info.filename),
                size=info.file_size,
            )
            for info in archive.infolist()
            if not info.is_dir()
        )

    def _parse_manifest(self, archive: ZipFile):
        """Read and parse app.json from the ZIP archive."""
        try:
            raw_manifest = archive.read(ZEPP_APP_JSON)
        except KeyError as exc:
            raise InvalidPackageError(
                f"Required manifest '{ZEPP_APP_JSON}' "
                "was not found in the archive."
            ) from exc

        try:
            manifest_text = raw_manifest.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise InvalidPackageError(
                f"Unable to decode '{ZEPP_APP_JSON}' as UTF-8."
            ) from exc

        return self._parser.parse(manifest_text)