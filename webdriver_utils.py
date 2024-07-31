from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver() -> webdriver.Chrome:
    """
    Returns a configured WebDriver instance with the necessary options.

    :return: The WebDriver instance.
    """
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--use-fake-ui-for-media-stream')
    options.add_argument('--disable-search-engine-choice-screen')

    driver = webdriver.Chrome(options=options)

    return driver
