from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest


# Arrange
@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_func_1(driver):
    driver.get("https://www.python.org")
    driver.implicitly_wait(3)
    search_input = driver.find_element(By.CLASS_NAME, "search-field")
    search_input.clear()


def test_func_2(driver):
    driver.get("https://duckduckgo.com")
    print(driver.title)
    search_input = driver.find_element("name", "q")
    search_input.send_keys("Selenium")
    search_input.send_keys(Keys.ENTER)


def test_func_3(driver):
    driver.get("https://www.uefa.com")
    driver.implicitly_wait(3)
