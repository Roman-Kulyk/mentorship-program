"""
Main Page Class for https://www.saucedemo.com/v1/
"""
from my_tests_v_1.lib.locators import *

class MainPage:
    def __init__(self, webdriver):
        self.driver = webdriver

    def  open_page(self, LOGIN_PAGE_URL):
        # Open certain web page
        self.driver.get(LOGIN_PAGE_URL)
        self.driver.implicitly_wait(3)
