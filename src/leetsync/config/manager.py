from __future__ import annotations

import json
from pathlib import Path

from leetsync.config.models import Config, GitHubConfig


class ConfigManager:
    """Load LeetSync configuration."""

    def __init__(self) -> None:
        self.config_path = Path("config.json")

    def load(self) -> Config:

        with self.config_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return Config(
            github=GitHubConfig(
                client_id=data["github"]["client_id"],
                client_secret=data["github"]["client_secret"],
            )
        )