"""
Custom exceptions used by KOSPET WatchFace Studio.
"""

from __future__ import annotations


class KWFSError(Exception):
    """
    Base exception for the project.
    """


class InvalidPackageError(KWFSError):
    """
    The supplied archive is not a valid watchface package.
    """


class UnsupportedPackageError(KWFSError):
    """
    Unsupported watchface package format.
    """


class PackageNotFoundError(KWFSError):
    """
    Package file was not found.
    """


class InvalidManifestError(KWFSError):
    """
    app.json is missing or invalid.
    """


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