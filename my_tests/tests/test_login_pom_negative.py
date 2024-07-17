import pytest
from my_tests.pages.login_page import LoginPage
from my_tests.lib.locators import *
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

def test_login_functionality(chrome_browser:object, user_input:str,
                             password:str, is_valid:bool) -> None:
    """
    This is a method to verify login functionality.
    Parameters
    chrome_browser:self
    user_input:str
               Username to log in with
    password:str
               Password to log in with
    is_valid:bool
               Variable to declare if log in s/b successfull or not
    """

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
    login_page.verify_successfull_login(is_valid)

