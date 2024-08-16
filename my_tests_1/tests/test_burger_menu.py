import pytest
from my_tests_1.pages.login_page import *
from my_tests_1.pages.inventory_page import *
import time

@pytest.mark.parametrize('user_input,password',
                             [('standard_user', 'secret_sauce'),])

def test_burger(chrome_browser:object, user_input:str,
                             password:str) -> None:
    """
    This is a method to verify burger menu functionality.
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
    time.sleep(3)
       
    inventory_page = InventoryPage(driver)
    inventory_page.bm_button(BM_BUTTON)
    time.sleep(2)

    # click every item in burger menu
    inventory_page.bm_item(MI_2)
    time.sleep(2)
    driver.back()

    inventory_page.bm_item(MI_3)
    time.sleep(2)
    driver.back()

    inventory_page.bm_item(MI_1)
    time.sleep(2)
   
    inventory_page.bm_button(BM_BUTTON)
    time.sleep(2)

    inventory_page.bm_item(MI_4)
    time.sleep(2)
   
    inventory_page.bm_cross_button(BM_CROSS_BUTTON)
    time.sleep(2)