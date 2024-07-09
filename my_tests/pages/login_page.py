"""
Login Page Class for https://www.saucedemo.com/v1/
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize('user_input,password,is_valid',
                             [('standard_user', 'secret_sauce', True),
                              ('wrong_standard_user', 'secret_sauce', False),
                              ('standard_user', 'wrong_secret_sauce', False),
                              ('wrong_standard_user', 'wrong_secret_sauce',
                               False)])
class LoginPage:
    def __init__(self, webdriver):
        self.driver = webdriver

    def  open_page(self, url):
        # Open certain web page
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def enter_username(self, user_input):
        user_name_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='username']")
        assert user_name_input.is_displayed()
    
        user_name_input.clear()
        user_name_input.send_keys(user_input)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='password']")
        assert password_input.is_displayed()
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login(self):
        login_button = self.driver.find_element(By.XPATH,
                                        "//input[@value='LOGIN']")
        login_button.click()
        # login_button.send_keys(Keys.RETURN)

    def verify_successfull_login(self, is_valid):    
        if is_valid:
            WebDriverWait(self.driver, 10).until(EC.staleness_of(self.enter_username))
            try:
                assert self.login_button.is_displayed()
            except StaleElementReferenceException:
                print("Login button doesn't exist at the moment!")

        else:
            error_message = self.driver.find_element(By.XPATH,
                                        "//h3[@data-test='error']")
            assert error_message.is_displayed()
