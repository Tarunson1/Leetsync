from typing import Any

from leetsync.config.constants import GRAPHQL_URL
from leetsync.network.client import HTTPClient
from leetsync.models.submission import RecentSubmission
from .graphql import RECENT_SUBMISSIONS_QUERY


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
    def get_recent_submissions(self, username: str) -> list[RecentSubmission]:
        """
    Fetch the user's recent accepted LeetCode submissions.

    Args:
        username: LeetCode username.

    Returns:
        A list of RecentSubmission objects.
    """

        response = self.execute(
        query=RECENT_SUBMISSIONS_QUERY,
        variables={
            "username": username,
        },
    )

        submissions = response["data"]["recentAcSubmissionList"]

        return [
        RecentSubmission(
            id=item["id"],
            title=item["title"],
            title_slug=item["titleSlug"],
            timestamp=int(item["timestamp"]),
        )
        for item in submissions
    ]
