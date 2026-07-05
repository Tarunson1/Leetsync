from dataclasses import dataclass
"""
    Represents a recently accepted LeetCode submission.
"""
@dataclass(slots=True)
class RecentSubmission:

    id: str

    title: str

    title_slug: str

    timestamp: int