# from leetsync.auth.providers.playwright import PlaywrightProvider
# from leetsync.auth.storage import SessionStorage
# from leetsync.auth.validator import SessionValidator
# from leetsync.auth.models import AuthSession
# from leetsync.auth.github_session import GitHubSession
# from leetsync.auth.providers.github import GitHubProvider
# from leetsync.auth.github_validator import GitHubSessionValidator
# from leetsync.auth.context import AuthenticationContext
# class AuthenticationManager:
#     """Manage LeetCode authentication."""

#     def __init__(self) -> None:
#         self.storage = SessionStorage()
#         #Leetcode
#         self.provider = PlaywrightProvider()
#         self.validator = SessionValidator()
#         #github
#         self.github_provider = GitHubProvider()
#         self.github_validator = GitHubSessionValidator()

#     def authenticate_leetcode(self) -> AuthSession:
#         session = self.storage.load()

#         if session is not None:
#             try:
#                 return self.validator.validate(session)
#             except Exception:
#                 pass

#         session = self.provider.authenticate()

#         session = self.validator.validate(session)

#         self.storage.save(session)

#         return session
#     def authenticate_github(self) -> GitHubSession:
#         """
#     Authenticate the user with GitHub.

#     Flow:
#         1. Try loading an existing GitHub session.
#         2. Validate it.
#         3. If invalid or missing, authenticate using OAuth.
#         4. Save the new session.
#     """

#     # Step 1: Try loading a previously saved GitHub session
#         session = self.storage.load_github()

#         if session is not None:
#             try:
#                 return self.github_validator.validate(session)
#             except Exception:
#             # Saved session is invalid or expired.
#             # Continue with OAuth authentication.
#                 pass

#     # Step 2: Authenticate using GitHub OAuth
#         session = self.github_provider.authenticate()

#     # Step 3: Validate the new session
#         session = self.github_validator.validate(session)

#     # Step 4: Save for future runs
#         self.storage.save_github(session)

#         return session
        
#     def authenticate(self) -> AuthSession:
#         """
#     Authenticate the user.

#     Flow:
#         1. Try loading an existing session.
#         2. Validate it.
#         3. If invalid or missing, authenticate using Playwright.
#         4. Save the new session.
#     """

#     # Step 1: Try loading a previously saved session
#     #     session = self.storage.load()

#     #     if session is not None:
#     #         try:
#     #             return self.validator.validate(session)
#     #         except Exception:
#     #         # Saved session is invalid or expired.
#     #         # Continue to fresh authentication.
#     #             pass

#     # # Step 2: No valid saved session → authenticate again
#     #     session = self.provider.authenticate()

#     # # Step 3: Validate the new session
#     #     session = self.validator.validate(session)

#     # # Step 4: Save for future runs
#     #     self.storage.save(session)

#         return self.authenticate_leetcode()
#     def authenticate_all(self) -> AuthenticationContext:
#         """
#     Authenticate both LeetCode and GitHub.
#     """

#         return AuthenticationContext(
#         leetcode=self.authenticate_leetcode(),
#         github=self.authenticate_github(),
#     )