# """
# Domain model representing detailed information about a LeetCode submission.
# """

# from dataclasses import dataclass


# @dataclass(slots=True, frozen=True)
# class SubmissionDetails:
#     code: str
#     runtime: str
#     memory: str
#     language: str
#     question_id: str
#     title_slug: str
#     timestamp: int
"""
Domain model representing detailed information about a LeetCode submission.
"""

"""
Domain model representing detailed information about a LeetCode submission.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SubmissionDetails:
    submission_id: str
    question_id: str

    title: str
    title_slug: str
    difficulty: str

    language: str

    code: str

    runtime: str
    memory: str

    timestamp: int