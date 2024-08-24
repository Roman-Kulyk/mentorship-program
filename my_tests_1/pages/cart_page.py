from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage
from selenium.webdriver.common.by import By


class CartPage(MainPage):

    def __init__(self, driver):
        """
        This is a method to initialize instance of the CartPage class.
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

    def continue_shopping(self):
        """This is a method to define continue shopping button."""
        self.continue_shopping_button = self.driver.find_element(
            By.XPATH, CONTINUE_SHOPPING)
        self.continue_shopping_button.click()

    def checkout(self):
        """This is a method to define checkout button."""
        self.checkout_button = self.driver.find_element(
            By.XPATH, CHECKOUT)
        self.checkout_button.click()
