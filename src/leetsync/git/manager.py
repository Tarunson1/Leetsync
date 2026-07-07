"""
Git manager.

Coordinates Git operations.
"""

from git import Repo

from leetsync.git.commit import GitCommit
from leetsync.git.push import GitPush
from leetsync.git.github import GitHubRepository


class GitManager:
    """
    High-level Git manager.
    """

    def __init__(
        self,
        repository_url: str,
        repo_path: str = ".",
    ) -> None:

        self.github = GitHubRepository(
            repository_url,
            repo_path,
        )

        if self.github.exists():
            self.repo = self.github.open()
        else:
            self.repo = self.github.clone()

        self.committer = GitCommit(self.repo)
        self.pusher = GitPush(self.repo)

    def sync(
        self,
        message: str,
    ) -> None:
        """
        Synchronize repository with GitHub.
        """

        # Get latest changes
        self.github.pull()

        # Stage files
        self.committer.stage_all()

        # Nothing changed
        if not self.repo.is_dirty(untracked_files=True):
            print("No changes detected.")
            return

        # Commit
        self.committer.commit(message)

        # Push
        self.pusher.push()

        print("Repository synchronized successfully.")