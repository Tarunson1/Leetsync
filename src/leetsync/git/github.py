"""
GitHub repository management.
"""

from pathlib import Path

from git import Repo


class GitHubRepository:
    """
    Responsible for cloning and opening Git repositories.
    """

    def __init__(
        self,
        repository_url: str,
        local_path: str,
    ) -> None:

        self.repository_url = repository_url
        self.local_path = Path(local_path)

    def exists(self) -> bool:
        """
        Check whether a valid Git repository already exists.
        """

        return (
        self.local_path.exists()
        and (self.local_path / ".git").exists()
    )

    def clone(self) -> Repo:
        """
        Clone the GitHub repository.
        """

        if not self.exists():

            return Repo.clone_from(
            self.repository_url,
            self.local_path,
    )

        return self.open()

    def open(self) -> Repo:
        """
        Open existing repository.
        """

        return Repo(self.local_path)
    def pull(self) -> None:
        """
        Pull the latest changes from origin.
        """

        repo = self.open()

        origin = repo.remote(name="origin")

        origin.pull()