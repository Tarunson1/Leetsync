"""
README service.
"""

from leetsync.repository.readme_generator import ReadmeGenerator


class ReadmeService:
    """
    Service responsible for updating the repository README.
    """

    def __init__(self) -> None:
        self.generator = ReadmeGenerator()

    def update(
        self,
        total: int,
        easy: int,
        medium: int,
        hard: int,
        recent_problem: str,
    ) -> None:
        """
        Update the README statistics.
        """

        self.generator.generate(
            total=total,
            easy=easy,
            medium=medium,
            hard=hard,
            recent_problem=recent_problem,
        )
        