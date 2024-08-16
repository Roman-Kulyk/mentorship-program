from selenium.webdriver.common.by import By
from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage


class InventoryPage(MainPage):
    """
    Constructs all the necessary attributes for the InventoryPage object.
    Attributes:
    driver:obj
                It is an object of webdriver class.
    Methods:
    __init__
        This is a method to initialize instance of the LoginPage class.
    select_item
        This is a method to select proper item
    add_to_cart
        This is a method to add item to the cart
    go_to_pdp_link
        This is a method to to to product page
    side_bar
        This is a method to define side gamgurger menu
    sc_button
        This is a method to define cart button
    sc_number
        This is a method to define quantity of products in cart
    bm_button
        This is a method to define burger menu button
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
        self.inventory_item_name = self.driver.find_element(By.XPATH, locator) 
        self.inventory_item_name.click()

    def add_to_cart_pdp(self, locator):
        """This method defines adding product to cart from pdp."""
        add_to_cart_button = self.driver.find_element(By.XPATH,locator)
        add_to_cart_button.click()

    def sc_button(self, locator):
        """This is a method to define how to move to cart."""
        self.sc_container = self.driver.find_element(By.XPATH, locator)
        self.sc_container.click()

    def sc_number(self, locator):
        """This is a method to define quantity of products in cart."""
        self.sc_badge = self.driver.find_element(By.XPATH, locator)
        text = self.sc_badge.text
        return int(text)
    
    def bm_button(self, locator):
        """This is a method to define bm_button."""
        self.bur_m_button = self.driver.find_element(By.XPATH, locator)
        self.bur_m_button.click()

    def bm_cross_button(self, locator):
       """This is a method to define bm_cross_button"""
       self.bur_cross_button = self.driver.find_element(By.XPATH, locator)
       self.bur_cross_button.click()

    def bm_item(self, text):
        """This is a method to define bm items"""
        self.bur_item = self.driver.find_element(By.ID, text)
        self.bur_item.click()