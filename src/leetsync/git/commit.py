"""
Git commit operations.
"""

from git import Repo


class GitCommit:
    """
    Responsible for staging files and creating Git commits.
    """

    def __init__(
        self,
        repo: Repo,
    ) -> None:

        self.repo = repo

    def stage_all(self) -> None:
        """
        Stage all changed files.
        """

        self.repo.git.add(A=True)

    def commit(
        self,
        message: str,
    ) -> None:
        """
        Create a Git commit.

        Args:
            message:
                Commit message.
        """

        # Don't create empty commits
        if self.repo.is_dirty(untracked_files=True):

            self.repo.index.commit(message)