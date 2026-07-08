from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class GitHubConfig:
    """GitHub OAuth configuration."""

    client_id: str
    client_secret: str
    repository_url: str
    local_path: str


@dataclass(slots=True)
class Config:
    """Application configuration."""

    github: GitHubConfig