from playwright.sync_api import BrowserContext


class CookieExtractor:

    @staticmethod
    def extract(context: BrowserContext) -> dict[str, str]:

        cookies = {}

        for cookie in context.cookies():

            cookies[cookie["name"]] = cookie["value"]

        return cookies