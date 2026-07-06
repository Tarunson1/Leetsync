from leetsync.api.client import LeetCodeClient


def main() -> None:
    client = LeetCodeClient()

    submissions = client.get_recent_submissions("tarun100ni")

    for submission in submissions:
        print(submission)


if __name__ == "__main__":
    main()