from locators.login_locators import LoginLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def load(self):
        self.page.goto("https://example.com/login")

    def login(self, username, password):
        self.page.fill(LoginLocators.USERNAME_FIELD, username)
        self.page.fill(LoginLocators.PASSWORD_FIELD, password)
        self.page.click(LoginLocators.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.page.is_visible(LoginLocators.LOGGED_IN_INDICATOR)
