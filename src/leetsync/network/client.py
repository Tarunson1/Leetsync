from __future__ import annotations
from typing import Any
from leetsync.auth.models import AuthSession
import httpx


class HTTPClient:
    """Wrapper around httpx.Client to seamlessly inject authentication states."""

    def __init__(self, timeout: float = 30.0, session: AuthSession | None = None) -> None:
        self._client = httpx.Client(timeout=timeout)
        self._session = session

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    def _inject_auth_cookies(self, kwargs: dict[str, Any]) -> None:
        """Helper method to clean up cookie injection logic across verbs."""
        kwargs.setdefault("cookies", {})
        if self._session and hasattr(self._session, "cookies"):
            kwargs["cookies"].update(self._session.cookies)

    def post(self, url: str, **kwargs: Any) -> httpx.Response:
        self._inject_auth_cookies(kwargs)
        return self._client.post(url, **kwargs)

    def get(self, url: str, **kwargs: Any) -> httpx.Response:
        # Fixed: Now GET requests also pass your extracted LeetCode credentials!
        self._inject_auth_cookies(kwargs)
        return self._client.get(url, **kwargs)

    def close(self) -> None:
        self._client.close()