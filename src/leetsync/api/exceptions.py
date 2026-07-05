"""
Custom exceptions used by the API layer.
"""


class LeetCodeAPIError(Exception):
    """Base exception for LeetCode API."""


class AuthenticationError(LeetCodeAPIError):
    """Raised when authentication fails."""


class GraphQLRequestError(LeetCodeAPIError):
    """Raised when a GraphQL request fails."""