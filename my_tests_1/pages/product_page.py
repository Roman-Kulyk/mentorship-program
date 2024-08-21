from selenium.webdriver.common.by import By
from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

class ProductPage(MainPage):
    """
    Constructs all the necessary attributes for the ProductPage object.
    Attributes:
    driver:obj
                It is an object of webdriver class.
    Methods:
    __init__
        This is a method to initialize instance of the LoginPage class.
    
    add_to_cart_pdp
        This is a method to add item to the cart
    back_button_pdp
        This is a method to define the 'back' button.
    """
    
    def __init__(self, driver):
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        super().__init__(driver)

    def go_to_pdp_link(self, locator):
        """This is a method to define how to move to pdp."""
        self.inventory_item_name = self.driver.find_element(By.ID, locator) 
        self.inventory_item_name.click()
    
    def add_to_cart_pdp(self, locator):
        """This method defines adding product to cart from pdp."""
        add_to_cart_button = self.driver.find_element(By.XPATH,locator)
        add_to_cart_button.click()    

    def remove_pdp(self, locator):
        """This method defines removing item from cart through pdp.""" 
        remove_button = self.driver.find_element(By.XPATH, locator)   
        remove_button.click()
    
    def back_pdp(self, locator):
        """This method defines back button functionality of pdp. """    
        self.back_button_pdp = self.driver.find_element(By.XPATH, locator)
        self.back_button_pdp.click()