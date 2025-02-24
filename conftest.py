import pytest
import yaml
from utils.playwright_factory import PlaywrightFactory

@pytest.fixture(scope="session")
def config():
    """Load configuration from a YAML file for use across tests."""
    with open("data/config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="class")
def setup(request, config):
    """
    Setup fixture for initializing the Playwright browser.
    Uses the configuration loaded from the 'config' fixture.
    """
    # Initialize the Playwright browser with config values
    browser_name = config.get("browser", "chromium")
    headless = config.get("headless", True)
    factory = PlaywrightFactory(browser_name=browser_name, headless=headless)
    
    # Attach the page object to the test class
    request.cls.page = factory.page

    yield  # Test execution happens here

    # Teardown: close the browser after tests finish
    factory.close()
