from hostinger_page import initiate_24_months_plan_purchase
from webdriver_utils import get_chrome_driver


def test_initiate_24_months_plan_purchase() -> None:
    """
    Test the initiate_plan_purchase function.
    :return: None.
    """
    # Initialize the WebDriver using the utility function
    driver = get_chrome_driver()

    try:
        # Call the function to initiate the plan purchase process
        initiate_24_months_plan_purchase(driver)
    finally:
        # Ensure the WebDriver is closed after the test
        driver.quit()
