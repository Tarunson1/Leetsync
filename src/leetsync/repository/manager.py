import json
import os
import subprocess
from typing import Any

class RepositoryManager:
    """Manages local code file persistence and automated Git lifecycle operations."""

    def __init__(self, repo_path: str = ".", state_file: str = "sync_state.json") -> None:
        self.repo_path = os.path.abspath(repo_path)
        self.state_file = os.path.join(self.repo_path, state_file)
        self.state = self._load_state()

    def _load_state(self) -> dict[str, Any]:
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    data["known_ids"] = set(data.get("known_ids", []))
                    return data
            except (json.JSONDecodeError, KeyError):
                print("⚠️ Warning: State file corrupted. Re-initializing tracking data.")
        return { "last_sync_timestamp": 0, "known_ids": set() }

    def save_state(self) -> None:
        """Saves current state tracking registers to disk."""
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump({
                "last_sync_timestamp": self.state["last_sync_timestamp"],
                "known_ids": list(self.state["known_ids"])
            }, f, indent=4)

    def _get_extension(self, language: str) -> str:
        mapping = {
            "cpp": "cpp", "java": "java", "python": "py", "python3": "py",
            "c": "c", "csharp": "cs", "javascript": "js", "typescript": "ts",
            "ruby": "rb", "swift": "swift", "golang": "go", "scala": "scala",
            "kotlin": "kt", "rust": "rs", "php": "php", "sql": "sql"
        }
        return mapping.get(language.lower(), "txt")

    def save_to_disk(self, title_slug: str, code: str, language: str) -> str:
        """Saves code locally inside structured folders."""
        ext = self._get_extension(language)
        question_dir = os.path.join(self.repo_path, "solutions", title_slug)
        os.makedirs(question_dir, exist_ok=True)
        
        file_path = os.path.join(question_dir, f"solution.{ext}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        return file_path

    def git_commit(self, file_path: str, commit_message: str) -> None:
        """Adds and Commits changes to local git history safely."""
        try:
            subprocess.run(["git", "add", file_path], check=True, cwd=self.repo_path, capture_output=True)
            
            status = subprocess.run(["git", "status", "--porcelain"], check=True, cwd=self.repo_path, capture_output=True, text=True)
            if not status.stdout.strip():
                return  # Skip if there's nothing new to commit

            subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=self.repo_path, capture_output=True)
            print(f"    🚀 Git: Committed change locally: {commit_message}")
        except subprocess.CalledProcessError as e:
            print(f"    ❌ Git Commit Error: {e.stderr.decode().strip()}")

    def git_push(self) -> None:
        """Pushes all accumulated commits to remote repository once."""
        try:
            print("[*] Flushing accumulated commits to Git Remote...")
            subprocess.run(["git", "push", "origin", "main"], check=True, cwd=self.repo_path, capture_output=True)
            print("    🚀 Git: Remote repository updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"    ❌ Git Push Error: {e.stderr.decode().strip()}")