from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from leetsync.auth.github_session import GitHubSession
from leetsync.auth.models import AuthSession

APP_DIR = Path.home() / ".leetsync"

LEETCODE_AUTH_FILE = APP_DIR / "leetcode_session.json"
GITHUB_AUTH_FILE = APP_DIR / "github_session.json"


class SessionStorage:
    """Persist LeetCode and GitHub authentication sessions."""

    def __init__(self) -> None:
        APP_DIR.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # LeetCode
    # ------------------------------------------------------------------

    def save(self, session: AuthSession) -> None:
        data = {
            "username": session.username,
            "cookies": session.cookies,
            "authenticated_at": session.authenticated_at.isoformat(),
        }

        LEETCODE_AUTH_FILE.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8",
        )

    def load(self) -> AuthSession | None:
        if not LEETCODE_AUTH_FILE.exists():
            return None

        data = json.loads(
            LEETCODE_AUTH_FILE.read_text(encoding="utf-8")
        )

        return AuthSession(
            username=data["username"],
            cookies=data["cookies"],
            authenticated_at=datetime.fromisoformat(
                data["authenticated_at"]
            ),
        )

    # ------------------------------------------------------------------
    # GitHub
    # ------------------------------------------------------------------

    def save_github(
        self,
        session: GitHubSession,
    ) -> None:
        data = {
            "username": session.username,
            "access_token": session.access_token,
            "authenticated_at": session.authenticated_at.isoformat(),
        }

        GITHUB_AUTH_FILE.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8",
        )

    def load_github(self) -> GitHubSession | None:
        if not GITHUB_AUTH_FILE.exists():
            return None

        data = json.loads(
            GITHUB_AUTH_FILE.read_text(encoding="utf-8")
        )

        return GitHubSession(
            username=data["username"],
            access_token=data["access_token"],
            authenticated_at=datetime.fromisoformat(
                data["authenticated_at"]
            ),
        )