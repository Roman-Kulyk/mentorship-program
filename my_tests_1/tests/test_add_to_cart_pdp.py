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
        
    inventory_page = InventoryPage(driver)
    # Click all product page links
    pdp_links = ["item_0_title_link",
                 "item_1_title_link",
                 "item_2_title_link",
                 "item_3_title_link",
                 "item_4_title_link",
                 "item_5_title_link",]
    
    cart_page = CartPage(driver)
    product_page = ProductPage(driver)
    
    for pdp in pdp_links:
        # go to product page
        product_page.go_to_pdp_link(pdp)
        time.sleep(1)
        # add product to cart from pdp
        product_page.add_to_cart_pdp(ADD_TO_CART_PDP)
        time.sleep(1)
        
        inventory_page.cart_button(CART_BUTTON)
        # return back to the inventory page
        cart_page.continue_shopping(CONTINUE_SHOPPING)
        time.sleep(1)

    inventory_page.cart_button(CART_BUTTON)
    cart_page.checkout(CHECKOUT)
    time.sleep(3)
    driver.back