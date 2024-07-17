import pytest
from my_tests_v_1.pages.login_page import LoginPage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_tests_v_1.lib.locators import *
import time

@pytest.mark.parametrize('user_input,password,is_valid',
                             [('standard_user', 'secret_sauce', False),
                              ('', '', True),
                              ('', 'secret_sauce', True),
                              ('standard_user', '', True),
                              ('wrong_standard_user', 'secret_sauce', True),
                              ('standard_user', 'wrong_secret_sauce', True),
                              ('wrong_standard_user', 'wrong_secret_sauce',
                               True)])

def test_login_functionality(chrome_browser, user_input, password, is_valid):
    
    url = LOGIN_PAGE_URL
    login_page = LoginPage(chrome_browser)
    
    # Open Page
    login_page.open_page(LOGIN_PAGE_URL)

    # Enter Username and Password
    login_page.enter_username(user_input)
    login_page.enter_password(password)
    
    # Click Login
    login_page.click_login()
    time.sleep(1)

    # Verify Successful Login by checking the presence of a logout button
    
def verify_successfull_login(self, is_valid):
    
    if is_valid:
        WebDriverWait(self.driver, 5).until(EC.staleness_of(self.login_button))
        try:
            assert self.login_button.is_displayed()
        except StaleElementReferenceException:
            print("Login button doesn't exist at the moment!")

    else:
        assert self.error_message.is_displayed()