import pytest
from my_tests_1.pages.login_page import *
from my_tests_1.pages.inventory_page import *
from my_tests_1.pages.product_page import *
from my_tests_1.pages.cart_page import *
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
    
    pdp_links = [SL_1, SL_2, SL_3, SL_4, SL_5, SL_6]
    
    cart_page = CartPage(driver)

    for pdp in pdp_links:
        # go to product page
        inventory_page.go_to_pdp_link(pdp)
        time.sleep(1)
        # add product to cart
        inventory_page.add_to_cart_pdp(ADD_TO_CART_PDP)
        time.sleep(1)
    
        inventory_page.sc_button(CART_BUTTON)
        # return back to the inventory page
        cart_page.continue_shopping(CONTINUE_SHOPPING)
        time.sleep(1)

    inventory_page.sc_button(CART_BUTTON)
    # verify if the number of products on badge equal to number of added items
    assert inventory_page.sc_number(SC_BADGE) == len(pdp_links)
       
    cart_page.checkout(CHECKOUT)
    time.sleep(3)
    driver.back