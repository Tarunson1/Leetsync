from pathlib import Path


class FileWriter:
    """
    Responsible for writing LeetCode solutions to the repository.
    """

    EXTENSIONS = {
        "python": ".py",
        "python3": ".py",
        "cpp": ".cpp",
        "c": ".c",
        "java": ".java",
        "javascript": ".js",
        "typescript": ".ts",
        "go": ".go",
        "rust": ".rs",
        "kotlin": ".kt",
        "swift": ".swift",
    }

    def __init__(self, root: str = "leetcode-solutions"):
        self.root = Path(root)

    def write_solution(
        self,
        difficulty: str,
        problem_id: str,
        title_slug: str,
        language: str,
        source_code: str,
    ) -> Path:

        folder = self.root / difficulty / f"{problem_id}-{title_slug}"

        folder.mkdir(parents=True, exist_ok=True)

        extension = self.EXTENSIONS.get(language.lower(), ".txt")

        solution_file = folder / f"solution{extension}"

        solution_file.write_text(source_code, encoding="utf-8")

        return solution_file


if __name__ == "__main__":

    writer = FileWriter()

    writer.write_solution(
        difficulty="Easy",
        problem_id="0001",
        title_slug="two-sum",
        language="Python",
        source_code='print("Hello LeetSync")'
    )

    print("Solution saved successfully.")