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
    enter_username
    """
    def __init__(self, webdriver):
        self.driver = webdriver
        """
        This is a method to initialize instance of the LoginPage class.
        Parameters
        webdriver:object
                webdriver to initialize
        """

    def open_page(self, LOGIN_PAGE_URL):
        # Open certain web page
        self.driver.get(LOGIN_PAGE_URL)
        self.driver.implicitly_wait(3)
