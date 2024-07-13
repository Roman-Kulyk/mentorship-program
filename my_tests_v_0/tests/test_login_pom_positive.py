import pytest
from my_tests.pages.login_page import LoginPage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize('user_input,password,is_valid',
                             [('standard_user', 'secret_sauce', True),
                              ('', '', False),
                              ('', 'secret_sauce', False),
                              ('standard_user', '', False),
                              ('wrong_standard_user', 'secret_sauce', False),
                              ('standard_user', 'wrong_secret_sauce', False),
                              ('wrong_standard_user', 'wrong_secret_sauce',
                               False)])

def test_login_functionality(chrome_browser, user_input, password, is_valid):
    url = "https://www.saucedemo.com/v1/"
    login_page = LoginPage(chrome_browser)
    
    # Open Page
    login_page.open_page(url)

    # Enter Username and Password
    login_page.enter_username(user_input)
    login_page.enter_password(password)
    
    # Click Login
    login_page.click_login()
    time.sleep(3)

    # Verify Successful Login by checking the presence of a logout button
    login_page.verify_successfull_login(is_valid)

def verify_successfull_login(self, is_valid):
    
    if is_valid:
        WebDriverWait(self.driver, 10).until(EC.staleness_of(self.user_name_input))
        try:
            assert self.login_button.is_displayed()
        except StaleElementReferenceException:
            print("Login button doesn't exist at the moment!")

    else:
        assert self.error_message.is_displayed()
    

    
    