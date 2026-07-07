from playwright.sync_api import sync_playwright


class BrowserManager:
    """Manage Playwright browser lifecycle."""

    def launch(self):
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=False,
        )

        context = browser.new_context()

        page = context.new_page()

        return playwright, browser, context, page