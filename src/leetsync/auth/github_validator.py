# from __future__ import annotations

# from leetsync.auth.github_session import GitHubSession
# from leetsync.config.constants import GITHUB_USER_URL
# from leetsync.network.client import HTTPClient


# class GitHubSessionValidator:
#     """Validate a stored GitHub session."""

#     def __init__(self) -> None:
#         self.http = HTTPClient()

#     def validate(
#         self,
#         session: GitHubSession,
#     ) -> GitHubSession:

#         response = self.http.get(
#             GITHUB_USER_URL,
#             headers={
#                 "Authorization": f"Bearer {session.access_token}",
#                 "Accept": "application/vnd.github+json",
#             },
#         )

#         response.raise_for_status()

#         user = response.json()

#         session.username = user["login"]

#         return session