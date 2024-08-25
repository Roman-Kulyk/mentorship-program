from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage
from selenium.webdriver.common.by import By


class CheckoutPage3(MainPage):

    def __init__(self, driver):
        """
        This is a method to initialize instance of the CheckoutPage3 class.
        Parameters
        webdriver:object
                webdriver to initialize
        Methods:
        pony_express_image
            This is a method to define pony express image
        """
        super().__init__(driver)

    def pony_express_image(self) -> None:
        """This is a method to find and click CONTINUE button on page."""
        self.pony_express = self.driver.find_element(
            By.XPATH, PONY_EXPRESS)
