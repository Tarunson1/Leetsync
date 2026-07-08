"""
Git push operations.
"""

from git import Repo


class GitPush:
    """
    Responsible for pushing commits to GitHub.
    """

    def __init__(
        self,
        repo: Repo,
    ) -> None:

        self.repo = repo

    # def push(self) -> None:
    #     """
    #     Push current branch to origin.
    #     """

    #     origin = self.repo.remote(name="origin")

    #     origin.push()

    def push(self) -> None:
        repo = self.repo

        repo.git.push("origin", "udaysingh-final")