# from leetsync.api.client import LeetCodeClient


# def main() -> None:
#     client = LeetCodeClient()

#     submissions = client.get_recent_submissions("tarun100ni")

#     for submission in submissions:
#         print(submission)


# if __name__ == "__main__":
#     main()

# from leetsync.api.client import LeetCodeClient
# from leetsync.api.graphql import SUBMISSION_DETAILS_QUERY


# client = LeetCodeClient()

# response = client.execute(
#     query=SUBMISSION_DETAILS_QUERY,
#     variables={
#         "submissionId": 2057319168,
#     },
# )

# print(response)

# from leetsync.auth.edge import EdgeSessionProvider

# provider = EdgeSessionProvider()

# cookies = provider.load()

# for cookie in cookies:
#     print(cookie.name)

import httpx

from leetsync.config.constants import GRAPHQL_URL
from leetsync.api.graphql import SUBMISSION_DETAILS_QUERY

cookies = {
    "LEETCODE_SESSION": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMTY3NzYyODMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJkMjJkOWEzMjJlNjNjYTQ5N2Q5MThlN2Q0MTUyOWRlNDZmNjE5NjIzOTk3OGE0NWI4NDdjZjExNTJhNWYzNDAiLCJzZXNzaW9uX3V1aWQiOiJjN2JjMmU0MiIsImlkIjoxNjc3NjI4MywiZW1haWwiOiJzdC50YXJ1bnNvbmlAYXJ5YWNvbGxlZ2UuZWR1LmluIiwidXNlcm5hbWUiOiJ0YXJ1bjEwMG5pIiwidXNlcl9zbHVnIjoidGFydW4xMDBuaSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy90YXJ1bjEwMG5pL2F2YXRhcl8xNzY2MTY4OTU3LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc4MzM2NTIzMCwiaXAiOiI0Ny4xNS44Ni4xNjgiLCJpZGVudGl0eSI6IjczYzJlMjFjMGZjNDdmODg0MWFhNjAwMGFmMWU2NGM3IiwiZGV2aWNlX3dpdGhfaXAiOlsiYjY5NDQ2ODdhYjI2YTRkODYxMTVmNjExNjM5NTZiYzQiLCI0Ny4xNS44Ni4xNjgiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.kIyXaUqFvUaqWdJHLhrYtSQ08rV9jQuPCYH-gY1YyCY",
    "csrftoken": "sYhiyJmQIHR2GOmIL4dtVRm3z7drjsL3",
}

headers = {
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/problems/two-sum/submissions/2058483722/",
    "X-CSRFToken": cookies["csrftoken"],
    "x-operation-name": "submissionDetails",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
    ),
}

client = httpx.Client(cookies=cookies, headers=headers)

response = client.post(
    GRAPHQL_URL,
    json={
        "query": SUBMISSION_DETAILS_QUERY,
        "variables": {
            "submissionId": 2058483722,
        },
    },
)

print(response.status_code)
print(response.json())