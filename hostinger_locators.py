from selenium.webdriver.common.by import By


class HOSTINGERLocators:
    COOKIES_ACCEPT = (By.XPATH, "//button[text()='Accept']")
    ADD_TO_CART = (By.XPATH, "(//button[contains(@class, 'h-button-primary') and contains(@class, 'h-pricing-card__add-to-cart')])[2]")
    MONTHS_SELECT = (By.XPATH, "//span[@class='up-body cart-period__period' and text()='24 months']")
    EMAIL_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='Email address']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='Password']/following-sibling::input")
    FIRST_NAME_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='First name (optional)']/following-sibling::input")
    LAST_NAME_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='Last name (optional)']/following-sibling::input")
    CITY_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='City (optional)']/following-sibling::input")
    STREET_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='Street address (optional)']/following-sibling::input")
    PHONE_NUMBER_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='Phone number (optional)']/following-sibling::input")
    ZIPCODE_INPUT = (By.XPATH, "//div[@class='h-form-field-label' and text()='ZIP code (optional)']/following-sibling::input")
    NAME_ON_CARD_INPUT = (By.XPATH, "//input[@id='cardholdername' and @placeholder='Name on card']")
    FIRST_IFRAME = (By.XPATH, "(//iframe[contains(@class, 'processout-field-cc-iframe')])[1]")
    CREDIT_CARD_INPUT = (By.XPATH, "//input[@type='tel' and @placeholder='0000 0000 0000 0000']")
    SECOND_IFRAME = (By.XPATH, "(//iframe[contains(@class, 'processout-field-cc-iframe')])[2]")
    THIRD_IFRAME = (By.XPATH, "(//iframe[contains(@class, 'processout-field-cc-iframe')])[3]")
    MONTH_YEAR_INPUT = (By.XPATH, "//input[@id='processout-field' and @placeholder='MM / YY']")
    CVC_INPUT = (By.XPATH, "//input[@type='tel' and @placeholder='CVC code']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error-message invalid') and text()='The card number is invalid.']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='hcart-submit-payment']")


