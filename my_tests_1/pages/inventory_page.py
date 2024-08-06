from selenium.webdriver.common.by import By
from my_tests_1.lib.constants import *
from my_tests_1.pages.main_page import MainPage


class InventoryPage(MainPage):
    
    def sl_backpack(self):
        price = 29.99
        sauce_labs_backpack = self.driver.find_element(By.XPATH, SL_1)
                
    def sl_bike_light(self):
        price = 9.99
        sauce_labs_bike_light = self.driver.find_element(By.XPATH, SL_2)
                
    def sl_bolt_tshirt(self):
        price = 15.99
        sauce_labs_bolt_tshirt = self.driver.find_element(By.XPATH, SL_3)

    def sl_fleese_jacket(self):
        price = 49.99
        sauce_labs_fleese_jacket = self.driver.find_element(By.XPATH, SL_4) 

    def sl_onesie(self):
        price = 7.99
        sauce_labs_onesie = self.driver.find_element(By.XPATH, SL_5)     
            
    def test_all_the_things(self):
        price = 15.99
        sauce_labs_test_all_the_things = self.driver.find_element(By.XPATH, SL_6)


    
    
    # OPTIONAL
    # def select_item(self, locator, price):
    #     self.price = price
    #     self.select_item = self.driver.find_element(By.XPATH,locator)
    #     self.add_to_cart.click()
    
    def add_to_cart(self, locator):
        add_to_cart_button = self.driver.find_element(By.XPATH,locator)
        add_to_cart_button.click()

    def go_to_product_page_link(self, locator):
        self.inventory_item_name = self.driver.find_element(By.XPATH, locator) 
        self.inventory_item_name.click()

    def side_bar(self):
        self.bm_menu = self.driver.find_element(By.XPATH, SIDE_BAR)
        self.bm_menu.click()

    def sort_product_cards(self):
        self.sort_product_card_link = self.driver.find_element(By.XPATH,
                                                           SORT_PRODUCT_CARDS)
        self.sort_product_cards_link.click()

    def cart_button(self):
        self.shopping_cart_container = self.driver.find_element(By.XPATH, CART_BUTTON)
        self.shopping_cart_container.click()