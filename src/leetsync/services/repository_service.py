"""
Repository service.

Acts as a bridge between the API layer and the repository layer.
"""

from leetsync.repository.manager import RepositoryManager
from leetsync.models.submission_details import SubmissionDetails


class RepositoryService:
    """
    Handles repository-related operations.
    """

    def __init__(self) -> None:
        self.manager = RepositoryManager()

    def save_submission(
        self,
        difficulty: str,
        details: SubmissionDetails,
    ) -> None:
        """
        Save a LeetCode submission to the local repository.

        Args:
            difficulty:
                Problem difficulty.

            details:
                Submission details object.
        """

        self.manager.save_submission(
            difficulty=difficulty,
            problem_id=details.question_id,
            title=details.title,
            title_slug=details.title_slug,
            language=details.language,
            source_code=details.code,
            runtime=details.runtime,
            memory=details.memory,
            submission_id=details.submission_id,
        )