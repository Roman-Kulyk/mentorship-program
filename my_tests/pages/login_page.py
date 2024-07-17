from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_tests.lib.constants import *
from my_tests.pages.main_page import MainPage


class LoginPage(MainPage):
    """
    Constructs all the necessary attributes for the LoginPage object.
    Methods:
    enter_username
        This is a method to find, clear and enter username into form
    enter_password
        This is a method to find, clear and enter password intor form
    click_login
        This is a method to find and click Login button on page
    error_message
        This is a method to find error message on page
    """

    def enter_username(self, user_input: str) -> None:
        """
        This is a method to find, clear and enter username into form.
        Parameters
        user_input:str
                   Username to log in with
        """

        self.user_name_input = self.driver.find_element(By.XPATH,
                                            ENTER_USERNAME_XPATH)
        self.user_name_input.clear()
        self.user_name_input.send_keys(user_input)

    def enter_password(self, password: str) -> None:
        """
        This is a method to find, clear and enter password into form.
        Parameters
        password:str
                 Password to log in with
        """
        password_input = self.driver.find_element(By.XPATH,
                                            ENTER_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self) -> None:
        """This is a method to find and click Login button on page."""
        self.login_button = self.driver.find_element(By.XPATH,
                                        CLICK_LOGIN)
        self.login_button.click()

    def error_message(self) -> None:
        """This is a method to find error message on page."""
        error_message = self.driver.find_element(By.XPATH,
                                    ERROR_MESSAGE)

    def verify_successfull_login(self, is_valid):
        """
        This is a method to verify if was log in successfull or not.
        Parameters
        is_valid:bool
            Variable to declare if log in s/b successfull or not
        """
        if is_valid:
            WebDriverWait(self.driver, 10).until(EC.staleness_of(self.user_name_input))
            try:
                assert self.login_button.is_displayed()
            except StaleElementReferenceException:
                print("Login button doesn't exist at the moment!")

        else:
            error_message = self.driver.find_element(By.XPATH,
                                        "//h3[@data-test='error']")
            assert error_message.is_displayed()
