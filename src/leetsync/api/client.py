from leetsync.network.client import HTTPClient


class LeetCodeClient:
    def __init__(self) -> None:
        self.http = HTTPClient()