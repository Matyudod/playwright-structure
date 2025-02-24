class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for an element to be visible on the page."""
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        """Click on an element specified by the selector."""
        self.wait_for_element(selector)
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill an input field specified by the selector."""
        self.wait_for_element(selector)
        self.page.fill(selector, text)

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible on the page."""
        try:
            self.page.wait_for_selector(selector, timeout=3000)
            return self.page.is_visible(selector)
        except Exception:
            return False

    def get_text(self, selector: str) -> str:
        """Get text content from an element."""
        self.wait_for_element(selector)
        return self.page.inner_text(selector)
