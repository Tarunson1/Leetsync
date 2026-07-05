from leetsync.api.client import LeetCodeClient
from leetsync.api.graphql import RECENT_SUBMISSIONS_QUERY


def main() -> None:
    client = LeetCodeClient()

    response = client.execute(
        query=RECENT_SUBMISSIONS_QUERY,
        variables={
            "username": "tarun100ni",
        },
    )

    print(response)


if __name__ == "__main__":
    main()