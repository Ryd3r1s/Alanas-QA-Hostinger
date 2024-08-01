import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.common.by import By


def wait_to_be_visible(driver: WebDriver, locator: tuple[str, str], timeout: int = 30) -> WebElement:
    """
    Waits for an element to be visible on the page.

    :param driver: The WebDriver instance.
    :param locator: The locator of the element as a tuple (By, value).
    :param timeout: The maximum time to wait for the element to be visible.
    :return: The WebElement if it becomes visible.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))


def click_element(driver: WebDriver, element_locator: tuple[str, str], scroll_into_view: bool = True) -> None:
    """
    Waits for an element to be visible, scrolls it into view (if necessary), and then clicks it.

    :param driver: The WebDriver instance.
    :param element_locator: The locator of the element as a tuple (By, value).
    :param scroll_into_view: If True, scrolls the element into view before clicking.
    :return: No return.
    """
    # Wait for the element to be visible
    element = wait_to_be_visible(driver, element_locator)

    # Scroll the element into view if necessary
    if scroll_into_view:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # Pause to ensure the scroll is complete (optional)
    time.sleep(2)

    # Click the element
    element.click()

    # Optional wait to ensure the action is registered
    time.sleep(3)


def fill_out_field(driver: WebDriver, field_locator: tuple[str, str], value: str) -> None:
    """
    Fills out the field with the provided value.

    :param driver: The WebDriver instance.
    :param field_locator: The locator of the field as a tuple (By, value).
    :param value: The value to fill out.
    :return: No return.
    """
    field = wait_to_be_visible(driver, field_locator)
    field.clear()
    field.send_keys(value)


def click_button(driver: WebDriver, locator: tuple[str, str]) -> None:
    """
    Waits for a button to be clickable and clicks it using the provided locator.
    :param driver: The WebDriver instance.
    :param locator: The locator of the button.
    :return: No return.
    """
    wait_to_be_visible(driver, locator).click()


def switch_to_iframe(driver: WebDriver, iframe_locator: tuple[str, str]) -> None:
    """
    Switches the WebDriver context to the specified iframe.

    :param driver: The WebDriver instance.
    :param iframe_locator: The locator of the iframe as a tuple (By, value).
    :return: None
    """
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(iframe_locator)
    )
    driver.switch_to.frame(iframe)


def switch_to_default_content(driver: WebDriver):
    """
    Switches back to the default content from any iframe.

    :param driver: The WebDriver instance.
    :return: None
    """
    driver.switch_to.default_content()


def select_random_option(driver, locator):
    """
    Selects a random option from a dropdown element specified by the locator.

    :param driver: The WebDriver instance used to interact with the web page.
    :param locator: A tuple containing the By strategy and the XPath for the dropdown options.
    """
    by, xpath = locator

    # Find all options using the locator
    options = driver.find_elements(by, xpath)

    # Select a random option and click it
    random_option = random.choice(options)
    random_option.click()
