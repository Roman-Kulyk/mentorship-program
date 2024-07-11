"""
Login Page Class for https://www.saucedemo.com/v1/
"""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from main_page import MainPage

class LoginPage:
    def __init__(self, webdriver):
        self.driver = webdriver

    
    def enter_username(self, user_input):
        self.user_name_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='username']")
        self.user_name_input.clear()
        self.user_name_input.send_keys(user_input)


    def enter_password(self, password):
        password_input = self.driver.find_element(By.XPATH,
                                            "//input[@data-test='password']")
        password_input.clear()
        password_input.send_keys(password)
    

    def click_login(self):
        self.login_button = self.driver.find_element(By.XPATH,
                                        "//input[@value='LOGIN']")
        self.login_button.click()
        
    
    def verify_successfull_login(self, is_valid):
        
        if is_valid:
            WebDriverWait(self.driver, 10).until(EC.staleness_of(self.user_name_input))
            try:
                assert self.login_button.is_displayed()
            except StaleElementReferenceException:
                print("Login button doesn't exist at the moment!")

        else:
            error_message = self.driver.find_element(By.XPATH,
                                        "//h3[@data-test='error']")
            assert error_message.is_displayed()