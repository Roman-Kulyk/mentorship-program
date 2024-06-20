from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pytest


# Arrange
@pytest.fixture(scope='session')
def driver():
    # Driver initialization
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_auth(driver):

    # Open certain web page
    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(3)

    # Find websearch element by id
    user_name_input = driver.find_element(By.ID, "user-name")
    user_name_input.clear()
    # Enter user name
    user_name_input.send_keys("standard_user")

    # Find websearch element by id
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    # Enter user name
    password_input.send_keys("secret_sauce")

    # Find websearch element by id
    login_button = driver.find_element(By.ID, "login-button")
    # Emulate press the Enter button
    login_button.send_keys(Keys.RETURN)

