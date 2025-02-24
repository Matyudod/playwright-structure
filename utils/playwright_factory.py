from playwright.sync_api import sync_playwright

class PlaywrightFactory:
    def __init__(self, browser_name="chromium", headless=True):
        self.playwright = sync_playwright().start()
        self.browser = getattr(self.playwright, browser_name).launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
