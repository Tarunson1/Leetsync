from __future__ import annotations

from leetsync.api.client import LeetCodeClient
from leetsync.api.graphql import USER_STATUS_QUERY
from leetsync.auth.models import AuthSession


class SessionValidator:
    """Validate a LeetCode session."""

    def validate(
        self,
        session: AuthSession,
    ) -> AuthSession:

        client = LeetCodeClient(session=session)

        response = client.execute(
            USER_STATUS_QUERY,
            {},
        )

        user = response.get("data", {}).get("userStatus")

        if not user:
            raise ValueError("Invalid response from LeetCode.")

        if not user["isSignedIn"]:
            raise ValueError("Authentication failed.")

        session.username = user["username"]

        return session