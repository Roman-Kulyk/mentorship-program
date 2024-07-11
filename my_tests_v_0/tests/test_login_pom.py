import pytest
from my_tests.pages.login_page import LoginPage

@pytest.mark.parametrize('user_input,password,is_valid',
                             [('standard_user', 'secret_sauce', True),
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

    # Verify Successful Login by checking the presence of a logout button
    login_page.verify_successfull_login(is_valid)
    