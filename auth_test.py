from leetsync.auth.manager import AuthenticationManager

manager = AuthenticationManager()

leetcode = manager.authenticate()

print(f"LeetCode: {leetcode.username}")

github = manager.authenticate_github()

print(f"GitHub: {github.username}")