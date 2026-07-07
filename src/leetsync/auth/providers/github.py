from __future__ import annotations
from leetsync.auth.callback_server import CallbackServer
from urllib.parse import urlencode
import webbrowser
from leetsync.network.client import HTTPClient
from leetsync.config.constants import GITHUB_TOKEN_URL,GITHUB_USER_URL
from datetime import datetime
from leetsync.config.manager import ConfigManager
from leetsync.auth.github_session import GitHubSession
from leetsync.auth.storage import SessionStorage
class GitHubProvider:
    """Authenticate with GitHub using OAuth."""

    AUTHORIZE_URL = "https://github.com/login/oauth/authorize"

    def __init__(self) -> None:
        self.config = ConfigManager().load()
        self.storage = SessionStorage()
        self.config = ConfigManager().load()
        self.http = HTTPClient()

    def authenticate(self) -> None:
        params = {
            "client_id": self.config.github.client_id,
            "redirect_uri": "http://localhost:8000/callback",
            "scope": "repo read:user",
        }

        url = (
            f"{self.AUTHORIZE_URL}"
            f"?{urlencode(params)}"
        )

        server = CallbackServer()
        print("Opening GitHub authorization page...")
        webbrowser.open(url)
        print("Waiting for GitHub authorization...")
        code = server.wait_for_code()  
        print(code)
        response = self.http.post(
    GITHUB_TOKEN_URL,
    headers={
        "Accept": "application/json",
    },
    data={
        "client_id": self.config.github.client_id,
        "client_secret": self.config.github.client_secret,
        "code": code,
    },
)

        response.raise_for_status()

        token = response.json()["access_token"]

        response = self.http.get(
            GITHUB_USER_URL,
            headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
    },
)

        response.raise_for_status()

        user = response.json()

        session = GitHubSession(
            username=user["login"],
            access_token=token,
        authenticated_at=datetime.now(),
)

        self.storage.save_github(session)

        return session