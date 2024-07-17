"""
Main Page Class for https://www.saucedemo.com/v1/
"""
from my_tests_v_0.lib.locators import *

class MainPage:
    def __init__(self, webdriver):
        self.driver = webdriver

    def  open_page(self, url):
        # Open certain web page
        self.driver.get(url)
        self.driver.implicitly_wait(3)