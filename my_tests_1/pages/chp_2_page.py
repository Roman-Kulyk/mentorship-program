from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage
from selenium.webdriver.common.by import By


class CheckoutPage2(MainPage):

    def __init__(self, driver):
        """
        This is a method to initialize instance of the CheckoutPage2 class.
        Parameters
        webdriver:object
                webdriver to initialize
        Methods:
        click_finish
            This is a method to define click FINISH button
        click_cancel
            This is a method to define click CANCEL button
        """
        super().__init__(driver)

    def click_finish(self) -> None:
        """This is a method to find and click FINISH button on page."""
        self.finish_button = self.driver.find_element(
            By.XPATH, FINISH)
        self.finish_button.click()

    def click_cancel(self) -> None:
        """This is a method to find and click CANCEL button on page."""
        self.cancel_button = self.driver.find_element(
            By.XPATH, CHP_2_CANCEL)
        self.cancel_button.click()
