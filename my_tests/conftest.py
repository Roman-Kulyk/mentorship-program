import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdrivermanager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def chrome_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()