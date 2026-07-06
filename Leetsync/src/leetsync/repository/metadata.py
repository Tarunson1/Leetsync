import json
from pathlib import Path


class MetadataWriter:
    """
    Responsible for creating metadata.json for every solution.
    """

    def __init__(self, root: str = "leetcode-solutions"):
        self.root = Path(root)

    def write_metadata(
        self,
        difficulty: str,
        problem_id: str,
        title: str,
        title_slug: str,
        language: str,
        runtime: str,
        memory: str,
        submission_id: str,
    ) -> Path:

        folder = self.root / difficulty / f"{problem_id}-{title_slug}"

        folder.mkdir(parents=True, exist_ok=True)

        metadata = {
            "problem_id": problem_id,
            "title": title,
            "title_slug": title_slug,
            "difficulty": difficulty,
            "language": language,
            "runtime": runtime,
            "memory": memory,
            "submission_id": submission_id,
        }

        metadata_file = folder / "metadata.json"

        with open(metadata_file, "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

        return metadata_file


if __name__ == "__main__":

    writer = MetadataWriter()

    writer.write_metadata(
        difficulty="Easy",
        problem_id="0001",
        title="Two Sum",
        title_slug="two-sum",
        language="Python",
        runtime="42 ms",
        memory="17 MB",
        submission_id="2057319168",
    )

    print("Metadata created successfully.")