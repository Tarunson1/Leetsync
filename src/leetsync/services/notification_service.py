"""
Notification service.
"""

from leetsync.notifications.console import Console


class NotificationService:
    """
    Handles console notifications.
    """

    def __init__(self) -> None:
        self.console = Console()

    def success(
        self,
        message: str,
    ) -> None:
        self.console.success(message)

    def error(
        self,
        message: str,
    ) -> None:
        self.console.error(message)

    def info(
        self,
        message: str,
    ) -> None:
        self.console.info(message)