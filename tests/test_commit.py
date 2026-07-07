from git import Repo
from leetsync.git.commit import GitCommit

repo = Repo(".")
commit = GitCommit(repo)

print("GitCommit loaded successfully")