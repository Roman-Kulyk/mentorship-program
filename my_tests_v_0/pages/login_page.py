"""
Login Page Class for https://www.saucedemo.com/v1/
"""
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, webdriver):
        self.driver = webdriver

    
    def enter_username(self, user_input):
        # self.user_name_input = self.driver.find_element(By.XPATH,
        #                                     "//input[@data-test='username']")
        self.user_name_input = self.driver.find_element(By.XPATH,
                                            ENTER_USERNAME_XPATH)
        self.user_name_input.clear()
        self.user_name_input.send_keys(user_input)


    def enter_password(self, password):
        # password_input = self.driver.find_element(By.XPATH,
        #                                     "//input[@data-test='password']")
        password_input = self.driver.find_element(By.XPATH,
                                            ENTER_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
    

    def click_login(self):
        # self.login_button = self.driver.find_element(By.XPATH,
        #                                 "//input[@value='LOGIN']")
        self.login_button = self.driver.find_element(By.XPATH,
                                        CLICK_LOGIN)
        self.login_button.click()

    def error_message(self):
        # error_message = self.driver.find_element(By.XPATH,
        #                             "//h3[@data-test='error']")
        error_message = self.driver.find_element(By.XPATH,
                                    ERROR_MESSAGE)
