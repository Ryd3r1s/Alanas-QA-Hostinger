import random
import string
import time

from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver

from hostinger_helpers import fill_out_field, click_button, switch_to_iframe, switch_to_default_content, \
    wait_to_be_visible, click_element
from hostinger_locators import HOSTINGERLocators


def initiate_24_months_plan_purchase(driver: WebDriver) -> None:
    """
    Function to initiate the plan purchase process.

    :param driver: An instance of WebDriver.
    :return: None
    """
    # Initialize the Faker library
    fake = Faker()

    # Open the target website
    driver.get("https://www.hostinger.com/web-hosting")

    time.sleep(2)
    click_button(driver, HOSTINGERLocators.COOKIES_ACCEPT)

    click_element(driver, HOSTINGERLocators.ADD_TO_CART)

    click_button(driver, HOSTINGERLocators.MONTHS_SELECT)

    # Generate a random email address with gmail.com domain
    random_username = fake.user_name()
    random_email = f"{random_username}@gmail.com"

    fill_out_field(driver, HOSTINGERLocators.EMAIL_INPUT, random_email)

    print(f"Random email '{random_email}' has been entered into the field.")

    fill_out_field(driver, HOSTINGERLocators.PASSWORD_INPUT, "Alanas_Sulskis-123!")

    random_first_name = fake.first_name()
    fill_out_field(driver, HOSTINGERLocators.FIRST_NAME_INPUT, random_first_name)

    random_last_name = fake.last_name()
    fill_out_field(driver, HOSTINGERLocators.LAST_NAME_INPUT, random_last_name)

    random_city = fake.city()
    fill_out_field(driver, HOSTINGERLocators.CITY_INPUT, random_city)

    random_street = fake.word()
    fill_out_field(driver, HOSTINGERLocators.STREET_INPUT, random_street)

    phone_number = '370' + ''.join(random.choices(string.digits, k=8))
    fill_out_field(driver, HOSTINGERLocators.PHONE_NUMBER_INPUT, phone_number)

    random_zipcode = fake.zipcode()
    fill_out_field(driver, HOSTINGERLocators.ZIPCODE_INPUT, random_zipcode)

    fill_out_field(driver, HOSTINGERLocators.NAME_ON_CARD_INPUT, random_username)

    # Switch to the first iframe for credit card input
    switch_to_iframe(driver, HOSTINGERLocators.FIRST_IFRAME)

    credit_card_number = (random.choices(string.digits, k=16))
    fill_out_field(driver, HOSTINGERLocators.CREDIT_CARD_INPUT, credit_card_number)

    switch_to_default_content(driver)

    # Switch to the second iframe for expiry date
    switch_to_iframe(driver, HOSTINGERLocators.SECOND_IFRAME)

    fill_out_field(driver, HOSTINGERLocators.MONTH_YEAR_INPUT, "0727")

    switch_to_default_content(driver)

    # Switch to the third iframe for CVC code
    switch_to_iframe(driver, HOSTINGERLocators.THIRD_IFRAME)

    fill_out_field(driver, HOSTINGERLocators.CVC_INPUT, "112")

    switch_to_default_content(driver)

    click_button(driver, HOSTINGERLocators.SUBMIT_BUTTON)

    try:
        error_message_element = wait_to_be_visible(driver, HOSTINGERLocators.ERROR_MESSAGE)

        # Assert that the error message is displayed
        assert error_message_element.is_displayed(), ("Test Failed: The error message for"
                                                      " an invalid card number was not found.")

        # If the assertion passes, print a success message
        print("Test Passed: Purchase failed because the card number is invalid.")

    except AssertionError as e:
        # Handle the failed assertion (optional)
        print(e)

    finally:
        # Ensure the browser is closed after the test
        driver.quit()

