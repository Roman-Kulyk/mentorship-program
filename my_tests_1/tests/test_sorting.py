import pytest
from my_tests_1.pages.login_page import *
from my_tests_1.pages.inventory_page import *
from my_tests_1.pages.product_page import *
from my_tests_1.pages.cart_page import *
import time


@pytest.mark.parametrize('user_input,password',
                             [('standard_user', 'secret_sauce'),])

def test_sorting(chrome_browser:object, user_input:str,
                             password:str) -> None:
    """
    This is a method to verify sorting functionality.
    Parameters
    chrome_browser:self
    user_input:str
               Username to log in with
    password:str
               Password to log in with
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
    time.sleep(1)
        
    inventory_page = InventoryPage(driver)
    
    # list of available options in dropdown
    sort_options = [SORT1, SORT2, SORT3, SORT4]
    for options in sort_options:
        inventory_page.sort_item(options)
        # verify if certain options is selected
        assert inventory_page.sort_menu_item.is_selected()
        assert inventory_page.sort_menu_item.is_displayed()
        assert inventory_page.sort_menu_item.is_enabled()
        time.sleep(3)