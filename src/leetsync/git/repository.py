"""
Repository management.
"""

from pathlib import Path

from git import Repo

from leetsync.git.github import GitHubRepository


class RepositoryManager:
    """
    Responsible for opening or cloning
    the GitHub repository.
    """

    def __init__(
        self,
        repository_url: str,
        local_path: str,
    ) -> None:

        self.github = GitHubRepository(
            repository_url,
            local_path,
        )

    def get_repository(self) -> Repo:
        """
        Return a local repository.

        If the repository does not exist,
        clone it first.
        """

        if self.github.exists():

            return self.github.open()

        return self.github.clone()