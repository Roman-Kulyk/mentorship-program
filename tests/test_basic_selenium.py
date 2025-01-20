from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_login_functionality(chrome_browser):
    """
    Test login functionality of the Practice Test Automaion website
    """
    url = "https://practicetestautomation.com/practice-test-login"

    # Navigate to the login page
    chrome_browser.get(url)

    # Find and fill the username and password fields
    chrome_browser.find_element(By.ID, "username").send_keys("student")
    chrome_browser.find_element(By.ID, "password").send_keys("Password123")

    # Find and click the logn button
    chrome_browser.find_element(By.ID, "submit").click()

    # Verify that the login was successful by checking the presence of
    # a logout button
    # Option 1: Locate by class name (if unique and reliable)
    try:
        logout_button = chrome_browser.find_element(
            By.CLASS_NAME, "wp-block-button__link"
        )
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."
