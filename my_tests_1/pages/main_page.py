from my_tests_1.lib.constants import *


class MainPage:
    """
    Constructs all the necessary attributes for the MainPage object.
    Attributes:
    webdriver:obj
                It is an object of webdriver class.
    Methods:
    __init__
        This is a method to initialize instance of the LoginPage class.
    open_page
        This is a method to open a certain web page.
    """
    def __init__(self, webdriver):
        """
        This is a method to initialize instance of the MainPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """
        self.driver = webdriver
        

    def open_page(self, url):
        """This is a method to open a certain web page."""
        self.driver.get(url)
        self.driver.implicitly_wait(3)
