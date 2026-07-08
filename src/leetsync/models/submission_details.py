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