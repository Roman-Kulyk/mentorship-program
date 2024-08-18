import pytest
from my_tests_1.pages.login_page import *
from my_tests_1.pages.inventory_page import *
from my_tests_1.pages.product_page import *
from my_tests_1.pages.cart_page import *
import time


@pytest.mark.parametrize('user_input,password',
                             [('standard_user', 'secret_sauce'),])

def test_add_to_cart_pdp(chrome_browser:object, user_input:str,
                             password:str) -> None:
    """
    This is a method to verify adding product to cart from pdp.
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
    time.sleep(1)
        
    pdp_links =[SLL_0, SLL_1, SLL_2, SLL_3, SLL_4, SLL_5]
    product_page = ProductPage(driver)
    
    for pdp in pdp_links:
        # go to product page
        product_page.go_to_pdp_link(pdp)
        time.sleep(1)
        # add product to cart from pdp
        product_page.add_to_cart_pdp(ADD_TO_CART_PDP)
        time.sleep(1)

        # remove product from cart
        product_page.remove_pdp(REMOVE_PDP)
        time.sleep(1)
        # return back to the inventory page
        driver.back()
        time.sleep(1)
