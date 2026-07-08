"""
Repository management.
"""

from leetsync.repository.structure import RepositoryStructure
from leetsync.repository.file_writer import FileWriter
from leetsync.repository.metadata import MetadataWriter
from leetsync.repository.readme_generator import ReadmeGenerator


class RepositoryManager:
    """
    Responsible for saving LeetCode solutions into
    the local repository.
    """

    def __init__(self) -> None:

        self.structure = RepositoryStructure()
        self.writer = FileWriter()
        self.metadata = MetadataWriter()
        self.readme = ReadmeGenerator()

    def save_submission(
        self,
        difficulty: str,
        problem_id: str,
        title: str,
        title_slug: str,
        language: str,
        source_code: str,
        runtime: str,
        memory: str,
        submission_id: str,
    ) -> None:
        """
        Save a complete submission into the repository.
        """

        # Initialize repository structure
        self.structure.initialize()

        # Save solution file
        self.writer.write_solution(
            difficulty=difficulty,
            problem_id=problem_id,
            title_slug=title_slug,
            language=language,
            source_code=source_code,
        )

        # Save metadata
        self.metadata.write_metadata(
            difficulty=difficulty,
            problem_id=problem_id,
            title=title,
            title_slug=title_slug,
            language=language,
            runtime=runtime,
            memory=memory,
            submission_id=submission_id,
        )

        # Update README
        self.readme.generate(
            total=1,
            easy=1 if difficulty == "Easy" else 0,
            medium=1 if difficulty == "Medium" else 0,
            hard=1 if difficulty == "Hard" else 0,
            recent_problem=title,
        )