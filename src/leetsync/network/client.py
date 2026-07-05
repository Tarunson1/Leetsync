from __future__ import annotations

import httpx


class HTTPClient:
    """Wrapper around httpx.Client."""

    def __init__(self, timeout: float = 30.0) -> None:
        self._client = httpx.Client(timeout=timeout)

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def post(self, url: str, **kwargs) -> httpx.Response:
        return self._client.post(url, **kwargs)

    def get(self, url: str, **kwargs) -> httpx.Response:
        return self._client.get(url, **kwargs)

    def close(self) -> None:
        self._client.close()