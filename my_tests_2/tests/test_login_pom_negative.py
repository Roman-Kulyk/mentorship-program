import pytest
from my_tests.pages.login_page import *
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_tests.lib.constants import *
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
    verify_successfull_login(chrome_browser, is_valid, login_page.user_name_input,
                             login_page.login_button)


def verify_successfull_login(driver, is_valid, user_name_input, login_button):
    """ 
    This is a method to verify if was log in successfull or not.
    Parameters
    is_valid:bool
        Variable to declare if log in s/b successfull or not
    """

    if is_valid:
        WebDriverWait(driver, 10).until(EC.staleness_of(user_name_input))
        try:
            assert login_button.is_displayed()
        except StaleElementReferenceException:
            print("Login button doesn't exist at the moment!")

    else:
        error_message = driver.find_element(By.XPATH,
                                    ERROR_MESSAGE)
        assert error_message.is_displayed()
