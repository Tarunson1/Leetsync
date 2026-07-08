"""
Repository service.

Acts as a bridge between the API layer and the repository layer.
"""

from leetsync.models.submission_details import SubmissionDetails
from leetsync.repository.manager import RepositoryManager


class RepositoryService:
    """
    Handles repository-related operations.
    """

    def __init__(self) -> None:
        self.manager = RepositoryManager()

    def save_submission(
        self,
        details: SubmissionDetails,
    ) -> None:
        """
        Save a LeetCode submission into the repository.
        """

        self.manager.save_submission(
            difficulty=details.difficulty,
            problem_id=details.question_id,
            title=details.title,
            title_slug=details.title_slug,
            language=details.language,
            source_code=details.code,
            runtime=details.runtime,
            memory=details.memory,
            submission_id=details.submission_id,
        )