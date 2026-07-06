from typing import Any

from leetsync.config.constants import GRAPHQL_URL
from leetsync.network.client import HTTPClient
from leetsync.models.submission import RecentSubmission
from leetsync.models.submission_details import SubmissionDetails
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
    
    def _map_recent_submission(
        self,
        item: dict[str, Any],
    ) -> RecentSubmission:
        """
        Convert a LeetCode API submission into a RecentSubmission model.
        """

        return RecentSubmission(
            id=item["id"],
            title=item["title"],
            title_slug=item["titleSlug"],
            timestamp=int(item["timestamp"]),
        )

    def _map_submission_details(
    self,
    item: dict[str, Any],
) -> SubmissionDetails:
        """
    Convert a LeetCode submission details response into a SubmissionDetails model.
    """

        return SubmissionDetails(
            code=item["code"],
            runtime=item["runtimeDisplay"],
            memory=item["memoryDisplay"],
            language=item["lang"]["name"],
            question_id=item["question"]["questionId"],
            title_slug=item["question"]["titleSlug"],
            timestamp=int(item["timestamp"]),
    )


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

    #     return [
    #     RecentSubmission(
    #         id=item["id"],
    #         title=item["title"],
    #         title_slug=item["titleSlug"],
    #         timestamp=int(item["timestamp"]),
    #     )
    #     for item in submissions
    # ]

        return [
    self._map_recent_submission(item)
    for item in submissions
]

    def get_submission_details():
        pass

    def validate_session():
        pass
