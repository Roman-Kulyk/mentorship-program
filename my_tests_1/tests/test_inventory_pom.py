import pytest
from my_tests_1.pages.login_page import *
from my_tests_1.pages.inventory_page import *
import time

@pytest.mark.parametrize('user_input,password',
                             [('standard_user', 'secret_sauce'),])

def test_login_functionality(chrome_browser:object, user_input:str,
                             password:str) -> None:
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
    driver = chrome_browser
    login_page = LoginPage(driver)
    # Open Page
    login_page.open_page(LOGIN_PAGE_URL)

    # Enter Username and Password
    login_page.enter_username(user_input)
    login_page.enter_password(password)

    # Click Login
    login_page.click_login()
    time.sleep(3)
        
    inventory_page = InventoryPage(driver)
    # Click Cart button
    inventory_page.cart_button()
    time.sleep(3)