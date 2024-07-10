import pytest
from my_tests.pages.login_page import LoginPage


def test_login_functionality(chrome_browser):
    url = "https://www.saucedemo.com/v1/"
    login_page = LoginPage(chrome_browser)
    # Open Page
    login_page.open_page(url)

    # Enter Username and Password
    
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')

    # Click Login
    login_page.click_login()

    # Verify Successful Login by checking the presence of a logout button
    login_page.verify_successfull_login(True)

