import pytest
from tests.pages.login_page import LoginPage


@pytest.mark.login
def test_login_functionality(chrome_browser):
    """
    Test the login functionality of the Practice Test Automation website
    """
    url = "https://practicetestautomation.com/practice-test-login/"
    login_page = LoginPage(chrome_browser)

    # Open Page
    login_page.open_page(url)

    # Enter Username and Password
    login_page.enter_username("student")
    login_page.enter_password("Password123")

    # Click Login
    login_page.click_login()

    # Verify Successful Login by checking the presence of a logout button
    assert login_page.verify_successful_login()
