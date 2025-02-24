import pytest
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestCheckout:
    def test_valid_checkout(self):
        checkout_page = CheckoutPage(self.page)
        checkout_page.load()  # Navigates to the checkout page
        checkout_page.fill_shipping_details({
            "first_name": "John",
            "last_name": "Doe",
            "address": "123 Main St",
            "city": "Anytown",
            "zip": "12345"
        })
        checkout_page.select_payment_method("credit_card")
        checkout_page.enter_payment_details({
            "card_number": "4111111111111111",
            "expiry_date": "12/25",
            "cvv": "123"
        })
        checkout_page.place_order()
        # Validate order success
        assert checkout_page.order_success_message_displayed(), "Order confirmation was not displayed"
