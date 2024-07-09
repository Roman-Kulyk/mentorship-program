import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()
