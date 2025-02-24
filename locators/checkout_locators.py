class CheckoutLocators:
    # Shipping Details
    FIRST_NAME = "input#firstName"          # CSS selector for the first name field
    LAST_NAME = "input#lastName"            # CSS selector for the last name field
    ADDRESS = "input#address"               # CSS selector for the address field
    CITY = "input#city"                     # CSS selector for the city field
    ZIP = "input#zip"                       # CSS selector for the ZIP/postal code field

    # Payment Methods
    PAYMENT_METHOD_CREDIT_CARD = "input#creditCard"  # CSS selector for credit card payment option
    PAYMENT_METHOD_PAYPAL = "input#paypal"           # CSS selector for PayPal payment option

    # Payment Details
    CARD_NUMBER = "input#cardNumber"        # CSS selector for the card number field
    EXPIRY_DATE = "input#expiryDate"        # CSS selector for the expiry date field
    CVV = "input#cvv"                       # CSS selector for the CVV field

    # Order Confirmation
    PLACE_ORDER_BUTTON = "button#placeOrder"  # CSS selector for the place order button
    ORDER_SUCCESS_MESSAGE = "div.order-success"  # CSS selector for the order success message
