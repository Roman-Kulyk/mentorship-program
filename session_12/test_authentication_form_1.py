from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import pytest


# Arrange
@pytest.fixture(scope='session')
def driver():
    # Driver initialization
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_successful_auth(driver):
    driver.maximize_window()
    # Open certain web page
    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(3)

    # Find websearch element by ID or XPATH
    # user_name_input = driver.find_element(By.ID, "user-name")
    user_name_input = driver.find_element(By.XPATH,
                                          "//input[@data-test='username']")
    assert user_name_input.is_displayed()
    user_name_input.clear()
    # Enter user name
    user_name_input.send_keys("standard_user")

    # Find websearch element by ID or XPATH
    # password_input = driver.find_element(By.ID, "password")
    password_input = driver.find_element(By.XPATH,
                                         "//input[@data-test='password']")
    assert password_input.is_displayed()
    password_input.clear()
    # Enter user name
    password_input.send_keys("secret_sauce")

    # Find websearch element by ID or XPATH
    # login_button = driver.find_element(By.ID, "login-button")
    login_button = driver.find_element(By.XPATH,
                                       "//input[@value='LOGIN']")
    assert login_button.is_displayed()
    # Emulate press the Enter button
    login_button.send_keys(Keys.RETURN)
    # Use an explicit wait with an expected condition to tell when one of your
    # login elements has gone stale
    WebDriverWait(driver, 10).until(EC.staleness_of(user_name_input))

    try:
        assert login_button.is_displayed()
    except StaleElementReferenceException:
        print('Login was successfull!')
