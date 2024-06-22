from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    user_name_input.clear()
    # Enter user name
    user_name_input.send_keys("wrong_standard_user")

    # Find websearch element by ID or XPATH
    # password_input = driver.find_element(By.ID, "password")
    password_input = driver.find_element(By.XPATH,
                                         "//input[@data-test='password']")
    password_input.clear()
    # Enter user name
    password_input.send_keys("secret_sauce")

    # Find websearch element by ID or XPATH
    # login_button = driver.find_element(By.ID, "login-button")
    login_button = driver.find_element(By.XPATH,
                                       "//input[@value='LOGIN']")
    # Emulate press the Enter button
    login_button.send_keys(Keys.RETURN)
    # Use an explicit wait with an expected condition to tell when one of your
    # login elements has gone stale
    WebDriverWait(driver, 10).until(EC.staleness_of(user_name_input))
