"""
Global constants used throughout the project.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

# ----------------------------------------------------------------------
# Project
# ----------------------------------------------------------------------

PROJECT_NAME: Final[str] = "KOSPET WatchFace Studio"

PACKAGE_NAME: Final[str] = "kospet_watchface_studio"

# ----------------------------------------------------------------------
# Supported package formats
# ----------------------------------------------------------------------

SUPPORTED_PACKAGE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".zip",
    ".bin",
)

# ----------------------------------------------------------------------
# Zepp package
# ----------------------------------------------------------------------

ZEPP_APP_JSON: Final[str] = "app.json"

ZEPP_APP_JS: Final[str] = "app.js"

ASSETS_DIRECTORY: Final[str] = "assets"

# ----------------------------------------------------------------------
# Image formats
# ----------------------------------------------------------------------

SUPPORTED_IMAGE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
)

# ----------------------------------------------------------------------
# Default encoding
# ----------------------------------------------------------------------

DEFAULT_ENCODING: Final[str] = "utf-8"

# ----------------------------------------------------------------------
# Internal folders
# ----------------------------------------------------------------------

CACHE_DIRECTORY: Final[Path] = Path(".kwfs")

TEMP_DIRECTORY: Final[Path] = CACHE_DIRECTORY / "tmp"

EXPORT_DIRECTORY: Final[Path] = CACHE_DIRECTORY / "export"

SUPPORTED_ARCHIVE_EXTENSIONS: Final[tuple[str, ...]] = (
    ".zip",
)