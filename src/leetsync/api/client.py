# from typing import Any
# from leetsync.auth.models import AuthSession
# from leetsync.config.constants import GRAPHQL_URL
# from leetsync.network.client import HTTPClient
# from leetsync.models.submission import RecentSubmission
# from leetsync.models.submission_details import SubmissionDetails
# from .graphql import RECENT_SUBMISSIONS_QUERY


# class LeetCodeClient:
#     """Client for interacting with the LeetCode GraphQL API."""

#     def __init__(self, session: AuthSession | None = None) -> None:
#         self.http = HTTPClient(session=session)

#     def execute(
#         self,
#         query: str,
#         variables: dict[str, Any],
#     ) -> dict[str, Any]:
#         """
#         Execute a GraphQL query.

#         Args:
#             query: GraphQL query string.
#             variables: Variables passed to the GraphQL query.

#         Returns:
#             Parsed JSON response.

#         Raises:
#             httpx.HTTPStatusError: If the request fails.
#         """

#         response = self.http.post(
#             GRAPHQL_URL,
#             json={
#                 "query": query,
#                 "variables": variables,
#             },
#         )

#         response.raise_for_status()

#         return response.json()
    
#     def _map_recent_submission(
#         self,
#         item: dict[str, Any],
#     ) -> RecentSubmission:
#         """
#         Convert a LeetCode API submission into a RecentSubmission model.
#         """

#         return RecentSubmission(
#             id=item["id"],
#             title=item["title"],
#             title_slug=item["titleSlug"],
#             timestamp=int(item["timestamp"]),
#         )

#     def _map_submission_details(
#     self,
#     item: dict[str, Any],
# ) -> SubmissionDetails:
#         """
#     Convert a LeetCode submission details response into a SubmissionDetails model.
#     """

#         return SubmissionDetails(
#             code=item["code"],
#             runtime=item["runtimeDisplay"],
#             memory=item["memoryDisplay"],
#             language=item["lang"]["name"],
#             question_id=item["question"]["questionId"],
#             title_slug=item["question"]["titleSlug"],
#             timestamp=int(item["timestamp"]),
#     )


#     def get_recent_submissions(self, username: str) -> list[RecentSubmission]:
#         """
#     Fetch the user's recent accepted LeetCode submissions.

#     Args:
#         username: LeetCode username.

#     Returns:
#         A list of RecentSubmission objects.
#     """

#         response = self.execute(
#         query=RECENT_SUBMISSIONS_QUERY,
#         variables={
#             "username": username,
#         },
#     )

#         submissions = response["data"]["recentAcSubmissionList"]

#     #     return [
#     #     RecentSubmission(
#     #         id=item["id"],
#     #         title=item["title"],
#     #         title_slug=item["titleSlug"],
#     #         timestamp=int(item["timestamp"]),
#     #     )
#     #     for item in submissions
#     # ]

#         return [
#     self._map_recent_submission(item)
#     for item in submissions
# ]

#     def get_submission_details():
#         pass

    
# from typing import Any
# from leetsync.auth.models import AuthSession
# from leetsync.config.constants import GRAPHQL_URL
# from leetsync.network.client import HTTPClient
# from leetsync.models.submission import RecentSubmission
# from leetsync.models.submission_details import SubmissionDetails
# from .graphql import RECENT_SUBMISSIONS_QUERY
# from .graphql import SUBMISSION_DETAILS_QUERY
# SUBMISSION_DETAILS_QUERY = """
# query submissionDetails($submissionId: Int!) {
#     submissionDetails(submissionId: $submissionId) {
#         runtime
#         runtimeDisplay
#         runtimePercentile
#         memory
#         memoryDisplay
#         memoryPercentile
#         code
#         timestamp
#         statusCode
#         lang {
#             name
#             verboseName
#         }
#         question {
#             questionId
#             titleSlug
#         }
#         runtimeError
#         compileError
#     }
# }
# """

# class LeetCodeClient:
#     """Client for interacting with the LeetCode GraphQL API."""

#     def __init__(self, session: AuthSession | None = None) -> None:
#         self.http = HTTPClient(session=session)

#     def execute(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
#         response = self.http.post(
#             GRAPHQL_URL,
#             json={"query": query, "variables": variables},
#         )
#         response.raise_for_status()
#         return response.json()
    
#     def _map_recent_submission(self, item: dict[str, Any]) -> RecentSubmission:
#         return RecentSubmission(
#             id=item["id"],
#             title=item["title"],
#             title_slug=item["titleSlug"],
#             timestamp=int(item["timestamp"]),
#         )

#     def _map_submission_details(self, item: dict[str, Any]) -> SubmissionDetails:
#         return SubmissionDetails(
#             code=item["code"],
#             runtime=item["runtimeDisplay"],
#             memory=item["memoryDisplay"],
#             language=item["lang"]["name"],
#             question_id=item["question"]["questionId"],
#             title_slug=item["question"]["titleSlug"],
#             timestamp=int(item["timestamp"]),
#         )

#     def get_recent_submissions(
#         self, 
#         username: str, 
#         last_sync_timestamp: int = 0,
#         known_submission_ids: set[str] | None = None
#     ) -> list[RecentSubmission]:
#         """
#         Fetches submissions incrementally. Stops if it hits a previously synced timestamp 
#         AND the unique submission ID is already processed.
#         """
#         response = self.execute(
#             query=RECENT_SUBMISSIONS_QUERY,
#             variables={"username": username},
#         )

#         submissions = response.get("data", {}).get("recentAcSubmissionList", [])
#         new_submissions = []
#         ids_to_check = known_submission_ids or set()

#         for item in submissions:
#             item_id = str(item["id"])
#             item_timestamp = int(item["timestamp"])
            
#             # Condition: If the submission is older than our last sync time 
#             # AND we already have this exact submission ID stored, we can safely stop.
#             if item_timestamp <= last_sync_timestamp and item_id in ids_to_check:
#                 break
                
#             # If it's a new ID or a completely new timestamp window, capture it
#             if item_id not in ids_to_check:
#                 new_submissions.append(self._map_recent_submission(item))

#         return new_submissions

#     def get_submission_details(self, submission_id: int) -> SubmissionDetails | None:
#         response = self.execute(
#             query=SUBMISSION_DETAILS_QUERY,
#             variables={"submissionId": submission_id},
#         )
#         details_data = response.get("data", {}).get("submissionDetails")
#         if not details_data:
#             return None
#         return self._map_submission_details(details_data)

# from typing import Any
# from leetsync.auth.models import AuthSession
# from leetsync.config.constants import GRAPHQL_URL
# from leetsync.network.client import HTTPClient
# from leetsync.models.submission import RecentSubmission
# from leetsync.models.submission_details import SubmissionDetails
# from .graphql import RECENT_SUBMISSIONS_QUERY
# from .graphql import SUBMISSION_DETAILS_QUERY

# class LeetCodeClient:
#     """Client for interacting with the LeetCode GraphQL API."""

#     def __init__(self, session: AuthSession | None = None) -> None:
#         self.http = HTTPClient(session=session)

#     def execute(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
#         response = self.http.post(
#             GRAPHQL_URL,
#             json={"query": query, "variables": variables},
#         )
#         response.raise_for_status()
#         return response.json()
    
#     def _map_recent_submission(self, item: dict[str, Any]) -> RecentSubmission:
#         return RecentSubmission(
#             id=item["id"],
#             title=item["title"],
#             title_slug=item["titleSlug"],
#             timestamp=int(item["timestamp"]),
#         )

#     def _map_submission_details(self, item: dict[str, Any]) -> SubmissionDetails:
#         return SubmissionDetails(
#             code=item["code"],
#             runtime=item["runtimeDisplay"],
#             memory=item["memoryDisplay"],
#             language=item["lang"]["name"],
#             question_id=item["question"]["questionId"],
#             title_slug=item["question"]["titleSlug"],
#             timestamp=int(item["timestamp"]),
#         )

#     def get_recent_submissions(
#         self, 
#         username: str, 
#         last_sync_timestamp: int = 0,
#         known_submission_ids: set[str] | None = None
#     ) -> list[RecentSubmission]:
#         """
#         Fetches submissions incrementally. Stops if it hits a previously synced timestamp 
#         AND the unique submission ID is already processed.
#         """
#         response = self.execute(
#             query=RECENT_SUBMISSIONS_QUERY,
#             variables={"username": username},
#         )

#         submissions = response.get("data", {}).get("recentAcSubmissionList", [])
#         new_submissions = []
#         ids_to_check = known_submission_ids or set()

#         for item in submissions:
#             item_id = str(item["id"])
#             item_timestamp = int(item["timestamp"])
            
#             if item_timestamp <= last_sync_timestamp and item_id in ids_to_check:
#                 break
                
#             if item_id not in ids_to_check:
#                 new_submissions.append(self._map_recent_submission(item))

#         return new_submissions

#     def get_submission_details(self, submission_id: int) -> SubmissionDetails | None:
#         response = self.execute(
#             query=SUBMISSION_DETAILS_QUERY,
#             variables={"submissionId": submission_id},
#         )
#         details_data = response.get("data", {}).get("submissionDetails")
#         if not details_data:
#             return None
#         return self._map_submission_details(details_data)


import sys
import os
from datetime import datetime
from urllib import response

# Python path ko adjust karein taaki 'src' directory ke modules safely discover ho sakein
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Clean decoupled module imports
from typing import Any
from leetsync.auth.models import AuthSession
from leetsync.config.constants import GRAPHQL_URL
from leetsync.network.client import HTTPClient
from leetsync.models.submission import RecentSubmission
from leetsync.models.submission_details import SubmissionDetails
from .graphql import RECENT_SUBMISSIONS_QUERY
from .graphql import SUBMISSION_DETAILS_QUERY

class LeetCodeClient:
    """Client for interacting with the LeetCode GraphQL API."""

    def __init__(self, session: AuthSession | None = None) -> None:
        self.http = HTTPClient(session=session)

    def execute(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        response = self.http.post(
            GRAPHQL_URL,
            json={"query": query, "variables": variables},
        )
        response.raise_for_status()
        return response.json()
    
    def _map_recent_submission(self, item: dict[str, Any]) -> RecentSubmission:
        return RecentSubmission(
            id=item["id"],
            title=item["title"],
            title_slug=item["titleSlug"],
            timestamp=int(item["timestamp"]),
        )

    # def _map_submission_details(self, item: dict[str, Any]) -> SubmissionDetails:
    #     return SubmissionDetails(
    #         code=item["code"],
    #         runtime=item["runtimeDisplay"],
    #         memory=item["memoryDisplay"],
    #         language=item["lang"]["name"],
    #         question_id=item["question"]["questionId"],
    #         title_slug=item["question"]["titleSlug"],
    #         timestamp=int(item["timestamp"]),
    #     )
    def _map_submission_details(self,item: dict[str, Any],) -> SubmissionDetails:

        return SubmissionDetails(
        submission_id=str(item.get("timestamp")),
        question_id=item["question"]["questionId"],
        title=item["question"]["titleSlug"].replace("-", " ").title(),
        title_slug=item["question"]["titleSlug"],
        difficulty="Unknown",
        language=item["lang"]["name"],
        code=item["code"],
        runtime=item["runtimeDisplay"],
        memory=item["memoryDisplay"],
        timestamp=int(item["timestamp"]),)
       

    def get_recent_submissions(
        self, 
        username: str, 
        last_sync_timestamp: int = 0,
        known_submission_ids: set[str] | None = None
    ) -> list[RecentSubmission]:
        """
        Fetches submissions incrementally. Stops if it hits a previously synced timestamp 
        AND the unique submission ID is already processed.
        """
        response = self.execute(
            query=RECENT_SUBMISSIONS_QUERY,
            variables={"username": username},
        )

        submissions = response.get("data", {}).get("recentAcSubmissionList", [])
        new_submissions = []
        ids_to_check = known_submission_ids or set()

        for item in submissions:
            item_id = str(item["id"])
            item_timestamp = int(item["timestamp"])
            
            if item_timestamp <= last_sync_timestamp and item_id in ids_to_check:
                break
                
            if item_id not in ids_to_check:
                new_submissions.append(self._map_recent_submission(item))

        return new_submissions

    # def get_submission_details(self, submission_id: int) -> SubmissionDetails | None:
    #     response = self.execute(
    #         query=SUBMISSION_DETAILS_QUERY,
    #         variables={"submissionId": submission_id},
    #     )
    #     details_data = response.get("data", {}).get("submissionDetails")
    #     if not details_data:
    #         return None
    #     return self._map_submission_details(details_data)

    def get_submission_details(self, submission_id: int) -> SubmissionDetails | None:
        response = self.execute(
        query=SUBMISSION_DETAILS_QUERY,
        variables={"submissionId": submission_id},
        )

        # print("Submission Details Response:")
        # print(response)

        details_data = response.get("data", {}).get("submissionDetails")

        if not details_data:
            return None

        return self._map_submission_details(details_data)