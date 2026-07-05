from typing import Any

from leetsync.config.constants import GRAPHQL_URL
from leetsync.network.client import HTTPClient


class LeetCodeClient:
    """Client for interacting with the LeetCode GraphQL API."""

    def __init__(self) -> None:
        self.http = HTTPClient()

    def execute(
        self,
        query: str,
        variables: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute a GraphQL query.

        Args:
            query: GraphQL query string.
            variables: Variables passed to the GraphQL query.

        Returns:
            Parsed JSON response.

        Raises:
            httpx.HTTPStatusError: If the request fails.
        """

        response = self.http.post(
            GRAPHQL_URL,
            json={
                "query": query,
                "variables": variables,
            },
        )

        response.raise_for_status()

        return response.json()