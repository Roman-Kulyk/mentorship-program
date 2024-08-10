from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class TestHerokuapp:
    # Arrange
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()
    
    def test_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com")
        time.sleep(0.5)

        drag_and_drop = driver.find_element(By.LINK_TEXT,"Drag and Drop") 
        assert drag_and_drop.is_displayed()
        drag_and_drop.click()
        time.sleep(0.5)
        # get source element
        source_element = driver.find_element(By.ID,"column-a")
        # get target element
        target_element = driver.find_element(By.ID,"column-b")
        # initialize action chain object
        action = ActionChains(driver)
        # drag and drop the item
        action.drag_and_drop(source_element, target_element)
        # perform the operation
        action.perform()
        time.sleep(0.5)
        driver.back()

    def test_hovers(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com")
        action = ActionChains(driver)
        time.sleep(0.5)

        hovers = driver.find_element(By.LINK_TEXT,"Hovers")
        assert hovers.is_displayed()
        hovers.click()
        time.sleep(0.5)

        # get source element user_1
        user_1 = driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[1]")
        assert user_1.is_displayed()
        action.move_to_element(user_1)
        action.perform()
        time.sleep(0.5)

        user_1_view_profile = driver.find_element(By.LINK_TEXT, "View profile")
        assert user_1_view_profile.is_displayed()
        user_1_view_profile.click()
        time.sleep(0.5)
        driver.back()

        # get source element user_2
        user_2 = driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[2]")
        assert user_2.is_displayed()
        action.move_to_element(user_2)
        action.perform()
        time.sleep(0.5)

        user_2_view_profile = driver.find_element(By.LINK_TEXT, "View profile")
        assert user_2_view_profile.is_displayed()
        user_2_view_profile.click()
        time.sleep(0.5)
        driver.back()

        # get source element user_3
        user_3 = driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[3]")
        assert user_3.is_displayed()
        action.move_to_element(user_3)
        action.perform()
        time.sleep(0.5)

        user_3_view_profile = driver.find_element(By.LINK_TEXT, "View profile")
        assert user_3_view_profile.is_displayed()
        user_3_view_profile.click()
        time.sleep(0.5)
        driver.back()

    def test_horizontal_slider(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com")
        action = ActionChains(driver)
        time.sleep(0.5)
        
        horizontal_slider = driver.find_element(By.LINK_TEXT,"Horizontal Slider")
        assert horizontal_slider.is_displayed()
        horizontal_slider.click()
        time.sleep(0.5)

        horizontal_slider_element = driver.find_element(By.XPATH, 
                                                        "//input[@type = 'range']")
        assert horizontal_slider_element.is_displayed()
        action.click_and_hold(horizontal_slider_element).move_by_offset(55, 0).release()
        action.perform()
        action.perform()
        time.sleep(0.5)
        driver.back()
