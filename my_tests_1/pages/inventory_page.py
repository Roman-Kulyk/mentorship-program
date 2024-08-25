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
    go_to_pdp_link
        This is a method to to to product page
    add_to_cart
        This is a method to add item to the cart
    remove_pdp
        This method defines removing item from cart through pdp
    sc_button
        This is a method to define cart button
    sc_number
        This is a method to define quantity of products in cart
    bm_button
        This is a method to define burger menu button
    bm_cross_button
        This is a method to define  bm_cross_button
    bm_item
        This is a method to define bm items
    sort_item
        This is a method to define sorting functionality
    """

    def __init__(self, driver):
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        super().__init__(driver)

    def go_to_pdp_link(self, locator: str) -> None:
        """This is a method to define how to move to pdp."""
        self.inventory_item_name = self.driver.find_element(By.XPATH, locator)
        self.inventory_item_name.click()

    def add_to_cart_pdp(self, locator: str) -> None:
        """This method defines adding product to cart from pdp."""
        add_to_cart_button = self.driver.find_element(By.XPATH, locator)
        add_to_cart_button.click()

    def remove_pdp(self, locator: str) -> None:
        """This method defines removing item from cart through pdp."""
        remove_button = self.driver.find_element(By.XPATH, locator)
        remove_button.click()

    def sc_button(self) -> None:
        """This is a method to define how to move to cart."""
        self.sc_container = self.driver.find_element(By.XPATH, CART_BUTTON)
        self.sc_container.click()

    def sc_number(self) -> None:
        """This is a method to define quantity of products in cart."""
        self.sc_badge = self.driver.find_element(By.XPATH, SC_BADGE)
        text = self.sc_badge.text
        return int(text)

    def bm_button(self) -> None:
        """This is a method to define bm_button."""
        self.bur_m_button = self.driver.find_element(By.XPATH, BM_BUTTON)
        self.bur_m_button.click()

    def bm_cross_button(self) -> None:
        """This is a method to define bm_cross_button."""
        self.bur_cross_button = self.driver.find_element(
           By.XPATH, BM_CROSS_BUTTON)
        self.bur_cross_button.click()

    def bm_item(self, text: str) -> None:
        """This is a method to define bm items."""
        self.bur_item = self.driver.find_element(By.ID, text)
        self.bur_item.click()

    def sort_item(self, locator: str) -> None:
        """This is a method to define sorting functionality."""
        self.sort_menu_item = self.driver.find_element(By.XPATH, locator)
        self.sort_menu_item.click()
