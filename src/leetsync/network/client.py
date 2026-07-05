"""
Reusable HTTP client for LeetSync.
"""

from __future__ import annotations

import httpx


class HTTPClient:
    """Lightweight wrapper around httpx.Client."""

    def __init__(self, timeout: float = 30.0) -> None:
        self._client = httpx.Client(timeout=timeout)

    def post(self, url: str, **kwargs) -> httpx.Response:
        """Send a POST request."""
        return self._client.post(url, **kwargs)

    def get(self, url: str, **kwargs) -> httpx.Response:
        """Send a GET request."""
        return self._client.get(url, **kwargs)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()