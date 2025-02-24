from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators

class CheckoutPage(BasePage):
    def load(self):
        # Navigates to the checkout page URL (could also use config data)
        self.page.goto("https://example.com/checkout")

    def fill_shipping_details(self, details: dict):
        # Fill in the shipping details form fields
        self.page.fill(CheckoutLocators.FIRST_NAME, details.get("first_name", ""))
        self.page.fill(CheckoutLocators.LAST_NAME, details.get("last_name", ""))
        self.page.fill(CheckoutLocators.ADDRESS, details.get("address", ""))
        self.page.fill(CheckoutLocators.CITY, details.get("city", ""))
        self.page.fill(CheckoutLocators.ZIP, details.get("zip", ""))

    def select_payment_method(self, method: str):
        # Selects a payment method, e.g., credit card, PayPal, etc.
        if method.lower() == "credit_card":
            self.page.click(CheckoutLocators.PAYMENT_METHOD_CREDIT_CARD)
        elif method.lower() == "paypal":
            self.page.click(CheckoutLocators.PAYMENT_METHOD_PAYPAL)
        # Extend with additional payment methods as needed

    def enter_payment_details(self, payment: dict):
        # Enter payment details for credit card payments
        self.page.fill(CheckoutLocators.CARD_NUMBER, payment.get("card_number", ""))
        self.page.fill(CheckoutLocators.EXPIRY_DATE, payment.get("expiry_date", ""))
        self.page.fill(CheckoutLocators.CVV, payment.get("cvv", ""))

    def place_order(self):
        # Click on the place order button
        self.page.click(CheckoutLocators.PLACE_ORDER_BUTTON)

    def order_success_message_displayed(self) -> bool:
        # Check if the success message is visible
        return self.page.is_visible(CheckoutLocators.ORDER_SUCCESS_MESSAGE)
