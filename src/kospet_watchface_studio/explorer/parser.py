"""
Zepp app.json parser.

Parses watchface metadata from a Zepp app.json manifest.
"""

from __future__ import annotations

import json
#from pathlib import PurePosixPath
from typing import Any

from kospet_watchface_studio.constants import ZEPP_APP_JSON
from kospet_watchface_studio.exceptions import InvalidManifestError

from .models import (
    ManifestInfo,
    ManifestPlatform,
    ManifestVersion,
)


class ManifestParser:
    """Parse Zepp app.json manifests."""

    def parse(self, data: str) -> ManifestInfo:
        """
        Parse app.json content.

        Parameters
        ----------
        data:
            JSON document as text.

        Returns
        -------
        ManifestInfo
            Parsed manifest information.

        Raises
        ------
        InvalidManifestError
            If the JSON is invalid or required fields are missing.
        """
        try:
            raw: Any = json.loads(data)
        except json.JSONDecodeError as exc:
            raise InvalidManifestError(
                f"Invalid JSON in {ZEPP_APP_JSON}"
            ) from exc

        try:
            app = raw["app"]
            version = app["version"]

            platforms = tuple(
                ManifestPlatform(
                    name=platform["name"],
                    device_source=platform["deviceSource"],
                )
                for platform in raw["platforms"]
            )

            return ManifestInfo(
                id=app["appId"],
                name=app["appName"],
                app_type=app["appType"],
                version=ManifestVersion(
                    code=version["code"],
                    name=version["name"],
                ),
                design_width=raw["designWidth"],
                platforms=platforms,
            )

        except (KeyError, TypeError, ValueError) as exc:
            raise InvalidManifestError(
                f"Required fields are missing or invalid in {ZEPP_APP_JSON}"
            ) from exc