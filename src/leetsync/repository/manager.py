from structure import RepositoryStructure
from file_writer import FileWriter
from metadata import MetadataWriter
from readme_generator import ReadmeGenerator


class RepositoryManager:

    def __init__(self):

        self.structure = RepositoryStructure()
        self.writer = FileWriter()
        self.metadata = MetadataWriter()
        self.readme = ReadmeGenerator()

    def save_solution(
        self,
        difficulty,
        problem_id,
        title,
        title_slug,
        language,
        source_code,
        runtime,
        memory,
        submission_id,
    ):

        # Create Repository
        self.structure.initialize()

        # Save Solution
        self.writer.write_solution(
            difficulty,
            problem_id,
            title_slug,
            language,
            source_code,
        )

        # Save Metadata
        self.metadata.write_metadata(
            difficulty,
            problem_id,
            title,
            title_slug,
            language,
            runtime,
            memory,
            submission_id,
        )

        # Update README
        self.readme.generate(
            total=1,
            easy=1,
            medium=0,
            hard=0,
            recent_problem=title,
        )


if __name__ == "__main__":

    manager = RepositoryManager()

    manager.save_solution(
        difficulty="Easy",
        problem_id="0001",
        title="Two Sum",
        title_slug="two-sum",
        language="Python",
        source_code='print("Hello LeetSync")',
        runtime="42 ms",
        memory="17 MB",
        submission_id="2057319168",
    )

    print("Repository Manager executed successfully.")