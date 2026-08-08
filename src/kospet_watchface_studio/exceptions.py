"""
Custom exceptions used by KOSPET WatchFace Studio.
"""

from __future__ import annotations


class KWFSError(Exception):
    """
    Base exception for the project.
    """


class InvalidPackageError(KWFSError):
    """Raised when a watchface package is invalid."""


class UnsupportedPackageError(KWFSError):
    """Raised when a package format is not supported."""


class PackageNotFoundError(KWFSError):
    """
    Package file was not found.
    """


class InvalidManifestError(KWFSError):
    """Raised when app.json is invalid."""


class ResourceNotFoundError(KWFSError):
    """
    Required resource is missing.
    """


class ParserError(KWFSError):
    """
    Generic parser error.
    """


class AnalyzerError(KWFSError):
    """
    Generic analyzer error.
    """


class ExportError(KWFSError):
    """
    Export failed.
    """


class ConverterError(KWFSError):
    """
    Conversion failed.
    """