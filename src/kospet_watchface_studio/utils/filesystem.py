"""
Filesystem helper functions for KOSPET WatchFace Studio.
"""

from __future__ import annotations

from pathlib import Path

from kospet_watchface_studio.constants import (
    DEFAULT_ENCODING,
    SUPPORTED_PACKAGE_EXTENSIONS,
)
from kospet_watchface_studio.exceptions import PackageNotFoundError


def ensure_exists(path: Path) -> Path:
    """
    Ensure that a path exists.

    Raises
    ------
    PackageNotFoundError
        If the path does not exist.
    """
    if not path.exists():
        raise PackageNotFoundError(f"Path does not exist: {path}")

    return path


def is_file(path: Path) -> bool:
    """Return True if path is a regular file."""
    return path.is_file()


def is_directory(path: Path) -> bool:
    """Return True if path is a directory."""
    return path.is_dir()


def is_supported_package(path: Path) -> bool:
    """
    Return True if the file has a supported watchface extension.
    """
    return path.suffix.lower() in SUPPORTED_PACKAGE_EXTENSIONS


def read_text(path: Path, encoding: str = DEFAULT_ENCODING) -> str:
    """
    Read a UTF-8 text file.
    """
    ensure_exists(path)
    return path.read_text(encoding=encoding)


def file_size(path: Path) -> int:
    """
    Return file size in bytes.
    """
    ensure_exists(path)
    return path.stat().st_size


def human_size(size: int) -> str:
    """
    Convert bytes to a human-readable string.

    Examples
    --------
    1536 -> "1.5 KB"
    5242880 -> "5.0 MB"
    """
    units = ("B", "KB", "MB", "GB", "TB")

    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.1f} {unit}"

        value /= 1024


def list_files(directory: Path) -> list[Path]:
    """
    Return all files inside directory recursively.
    """
    ensure_exists(directory)

    return sorted(
        file
        for file in directory.rglob("*")
        if file.is_file()
    )


def find_files(
    directory: Path,
    suffix: str,
) -> list[Path]:
    """
    Find files by extension.

    Example
    -------
    find_files(path, ".png")
    """
    ensure_exists(directory)

    suffix = suffix.lower()

    return sorted(
        file
        for file in directory.rglob("*")
        if file.is_file() and file.suffix.lower() == suffix
    )