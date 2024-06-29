from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import pytest


class TestLoginPage:
    # Arrange
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    @pytest.mark.parametrize('user_input,password,is_valid',
                             [('standard_user', 'secret_sauce', True),
                              ('wrong_standard_user', 'secret_sauce', False),
                              ('standard_user', 'wrong_secret_sauce', False),
                              ('wrong_standard_user', 'wrong_secret_sauce',
                               False)])
    def test_successful_auth(self, user_input, password, is_valid):
        self.driver.maximize_window()
        # Open certain web page
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.implicitly_wait(3)

        # Find websearch element by ID or XPATH
        # user_name_input = self.driver.find_element(By.ID, "user-name")
        user_name_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='username']")
        user_name_input.clear()
        # Enter user name
        user_name_input.send_keys(user_input)

        # Find websearch element by ID or XPATH
        # password_input = self.driver.find_element(By.ID, "password")
        password_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='password']")
        password_input.clear()
        # Enter user name
        password_input.send_keys(password)

        # Find websearch element by ID or XPATH
        # login_button = self.driver.find_element(By.ID, "login-button")
        login_button = self.driver.find_element(By.XPATH,
                                        "//input[@value='LOGIN']")
        # Emulate press the Enter button
        login_button.send_keys(Keys.RETURN)

        if is_valid:
            # Use an explicit wait with an expected condition to tell when one
            # of your login elements has gone stale
            WebDriverWait(self.driver, 10).until(EC.staleness_of(user_name_input))
            try:
                assert login_button.is_displayed()
            except StaleElementReferenceException:
                print("Login button doesn't exist at the moment!")

        else:
            # Find websearch element by ID or XPATH
            error_message = self.driver.find_element(By.XPATH,
                                        "//h3[@data-test='error']")
            assert error_message.is_displayed()
