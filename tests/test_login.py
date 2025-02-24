import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.page)
        login_page.load()
        login_page.login("user@example.com", "password")
        assert login_page.is_logged_in()
