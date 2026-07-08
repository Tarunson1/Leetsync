"""
Synchronization engine.

Coordinates the complete synchronization process.
"""

from leetsync.services.repository_service import RepositoryService
from leetsync.services.readme_service import ReadmeService
from leetsync.services.notification_service import NotificationService
from leetsync.git.manager import GitManager
from leetsync.config.manager import ConfigManager
from leetsync.api.client import LeetCodeClient
from leetsync.auth.manager import AuthenticationManager


class SyncEngine:
    """
    Main synchronization engine.
    """

    def __init__(self) -> None:
        config = ConfigManager().load()

        # self.client = LeetCodeClient()
        auth = AuthenticationManager()

        leetcode_session = auth.authenticate()

        self.client = LeetCodeClient(
        session=leetcode_session
        )

        self.repository = RepositoryService()

        self.readme = ReadmeService()

        self.notifications = NotificationService()

        self.git = GitManager(
            repository_url=config.github.repository_url,
            repo_path=config.github.local_path,
        )

    def sync(self) -> None:
        """
        Synchronize the latest accepted submission.
        """

        self.notifications.info(
            "Synchronization started..."
        )
        print("Calling get_recent_submissions...")
        # Fetch recent submissions
        submissions = self.client.get_recent_submissions(
            # username="YOUR_LEETCODE_USERNAME"
            username="udaysingh01"
        )
        print("Submissions object:", submissions)

        if not submissions:
            self.notifications.info(
                "No recent submissions found."
            )
            return

        latest = submissions[0]

        details = self.client.get_submission_details(
            int(latest.id)
        )

        if details is None:
            self.notifications.error(
                "Unable to fetch submission details."
            )
            return

        # Save locally
        self.repository.save_submission(details)

        # Update README (optional)
        # self.readme.update()

        # Commit + Push
        self.git.sync(
            f"Solve {details.title}"
        )

        self.notifications.success(
            "Synchronization completed successfully."
        )