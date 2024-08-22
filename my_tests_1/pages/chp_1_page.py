from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage
from selenium.webdriver.common.by import By


class CheckoutPage1(MainPage):
    
    def __init__(self, driver):
        """
        This is a method to initialize instance of the CheckoutPage1 class.
        Parameters
        webdriver:object
                webdriver to initialize
        Methods:
        continue_shopping
            This is a method to define continue shopping button
        checkout
            This is a method to define checkout button
        """
        super().__init__(driver)

    def enter_first_name(self, first_name: str) -> None:
        """
        This is a method to find, clear and enter first name into form.
        Parameters
        first_name:str
                   First name to log in with
        """
        self.first_name_input = self.driver.find_element(By.XPATH, FIRST_NAME)
        self.first_name_input.clear()
        self.first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        This is a method to find, clear and enter last name into form.
        Parameters
        last_name:str
                   Last name to log in with
        """
        self.last_name_input = self.driver.find_element(By.XPATH, LAST_NAME)
        self.last_name_input.clear()
        self.last_name_input.send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """
        This is a method to find, clear and postal code into form.
        Parameters
        postal_code:str
                   postal_code to log in with
        """
        self.postal_code_input = self.driver.find_element(By.XPATH, ZIP)
        self.postal_code_input.clear()
        self.postal_code_input.send_keys(postal_code)

    def click_continue(self) -> None:
        """This is a method to find and click CONTINUE button on page."""
        self.continue_button = self.driver.find_element(By.XPATH,
                                        CONTINUE)
        self.continue_button.click()

    def click_cancel(self) -> None:
        """This is a method to find and click CANCEL button on page."""
        self.cancel_button = self.driver.find_element(By.XPATH,
                                        CHP_1_CANCEL)
        self.cancel_button.click()