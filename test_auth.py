from datetime import datetime

from leetsync.auth.models import AuthSession
from leetsync.auth.storage import SessionStorage

storage = SessionStorage()

session = AuthSession(
    username="tarun100ni",
    cookies={
        "LEETCODE_SESSION": "abc",
        "csrftoken": "xyz",
    },
    authenticated_at=datetime.now(),
)

storage.save(session)

loaded = storage.load()

print(loaded)