"""
GraphQL queries used by the LeetCode client.
"""

RECENT_SUBMISSIONS_QUERY = """
query recentAcSubmissionList($username: String!) {
    recentAcSubmissionList(username: $username) {
        id
        title
        titleSlug
        timestamp
    }
}
"""

SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {
        runtime
        runtimeDisplay
        runtimePercentile

        memory
        memoryDisplay
        memoryPercentile

        code
        timestamp
        statusCode

        lang {
            name
            verboseName
        }

        question {
            questionId
            titleSlug
        }

        runtimeError
        compileError
    }
}
"""

USER_STATUS_QUERY = """
query userStatus {
    userStatus {
        username
        isSignedIn
    }
}
"""