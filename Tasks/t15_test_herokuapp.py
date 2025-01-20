from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
from selenium.webdriver.support.ui import Select 

class TestHerokuapp:
    # Arrange
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.implicitly_wait(3)
        yield
        self.driver.quit()

    def test_drag_and_drop(self):
        drag_and_drop = self.driver.find_element(By.LINK_TEXT, "Drag and Drop")
        assert drag_and_drop.is_displayed()
        drag_and_drop.click()
        time.sleep(0.5)
        # get source element
        source_element = self.driver.find_element(By.ID, "column-a")
        # get target element
        target_element = self.driver.find_element(By.ID, "column-b")
        # initialize action chain object
        action = ActionChains(self.driver)
        # drag and drop the item
        action.drag_and_drop(source_element, target_element)
        # perform the operation
        action.perform()
        time.sleep(0.5)
        self.driver.back()

    def test_hovers(self):
        action = ActionChains(self.driver)

        hovers = self.driver.find_element(By.LINK_TEXT, "Hovers")
        assert hovers.is_displayed()
        hovers.click()
        time.sleep(0.5)

        # get source element user_1
        user_1 = self.driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[1]")
        assert user_1.is_displayed()
        action.move_to_element(user_1)
        action.perform()
        time.sleep(0.5)

        user_1_view_profile = self.driver.find_element(By.LINK_TEXT,
                                                    "View profile")
        assert user_1_view_profile.is_displayed()
        user_1_view_profile.click()
        time.sleep(0.5)
        self.driver.back()

        # get source element user_2
        user_2 = self.driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[2]")
        assert user_2.is_displayed()
        action.move_to_element(user_2)
        action.perform()
        time.sleep(0.5)

        user_2_view_profile = self.driver.find_element(By.LINK_TEXT,
                                                    "View profile")
        assert user_2_view_profile.is_displayed()
        user_2_view_profile.click()
        time.sleep(0.5)
        self.driver.back()

        # get source element user_3
        user_3 = self.driver.find_element(By.XPATH,
                                    "(//div[@class='figure'])[3]")
        assert user_3.is_displayed()
        action.move_to_element(user_3)
        action.perform()
        time.sleep(0.5)

        user_3_view_profile = self.driver.find_element(By.LINK_TEXT,
                                                    "View profile")
        assert user_3_view_profile.is_displayed()
        user_3_view_profile.click()
        time.sleep(0.5)
        self.driver.back()

    def test_horizontal_slider(self):

        action = ActionChains(self.driver)

        horizontal_slider = self.driver.find_element(By.LINK_TEXT,
                                                    "Horizontal Slider")
        assert horizontal_slider.is_displayed()
        horizontal_slider.click()
        time.sleep(0.5)

        horizontal_slider_element = self.driver.find_element(By.XPATH,
                                                    "//input[@type = 'range']")
        assert horizontal_slider_element.is_displayed()
        action.click_and_hold(horizontal_slider_element).move_by_offset(55, 0).release()
        action.perform()
        action.perform()
        time.sleep(0.5)
        self.driver.back()

    def test_scroll(self):

        infininte_scroll = self.driver.find_element(By.LINK_TEXT,
                                                    'Infinite Scroll')
        assert infininte_scroll.is_displayed()
        infininte_scroll.click()
        time.sleep(0.5)
        # scroll down by pixel
        self.driver.execute_script("window.scrollBy(0, 2500);")
        time.sleep(0.5)
        self.driver.back()

    def test_checkboxes(self):
        checkboxes_button = self.driver.find_element(By.LINK_TEXT,
                                                     "Checkboxes")
        assert checkboxes_button.is_displayed()
        checkboxes_button.click()
        time.sleep(0.5)
        cb1_button = self.driver.find_element(By.XPATH,
                                            "(//input[@type = 'checkbox'])[1]")
        cb1_button.click()
        time.sleep(0.5)
        assert cb1_button.is_selected()
        assert cb1_button.is_displayed()
        assert cb1_button.is_enabled()
        cb2_button = self.driver.find_element(By.XPATH,
                                            "(//input[@type = 'checkbox'])[2]")
        assert cb2_button.is_selected()
        assert cb2_button.is_displayed()
        assert cb2_button.is_enabled()

    # def test_dropdown_list(self): # Option #1 using XPATH
    #     dd_list_page = self.driver.find_element(By.LINK_TEXT, "Dropdown")
    #     assert dd_list_page.is_displayed()
    #     dd_list_page.click()
    #     time.sleep(0.5)

    #     dropdown_list = self.driver.find_element(By.ID, "dropdown")
    #     assert dropdown_list.is_displayed()
    #     dropdown_list.click()
    #     time.sleep(0.5)

    #     dropdown_list_opt1 = self.driver.find_element(By.XPATH,
    #                                                 "(//option[@value = '1'])")
    #     dropdown_list_opt2 = self.driver.find_element(By.XPATH,
    #                                                 "(//option[@value = '2'])")
           
    #     dropdown_list_opt1.click()
    #     assert dropdown_list_opt1.is_enabled()
    #     assert dropdown_list_opt1.is_selected()
    #     time.sleep(3)

    #     dropdown_list_opt2.click()
    #     assert dropdown_list_opt2.is_enabled()
    #     assert dropdown_list_opt2.is_selected()
    #     time.sleep(3)

    def test_dropdown_list(self): # Option #2 using Select module
        dd_list_page = self.driver.find_element(By.LINK_TEXT, "Dropdown")
        assert dd_list_page.is_displayed()
        dd_list_page.click()
        time.sleep(0.5)
      
        dropdown_list = self.driver.find_element(By.ID, "dropdown")
        assert dropdown_list.is_displayed()
        dropdown_list.click()
        # Create an object of the select class
        drop = Select(dropdown_list)

        # Select by index first option
        drop.select_by_index(1) 
        time.sleep(2)
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 1', 'Selected option should be Option 1'
        # Select by index second option
        drop.select_by_index(2)
        time.sleep(2)
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 2', 'Selected option should be Option 2'
        
        # Select by value first option 
        drop.select_by_value("1") 
        time.sleep(2) 
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 1', 'Selected option should be Option 1'
        # Select by value second option
        drop.select_by_value("2")
        time.sleep(2)
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 2', 'Selected option should be Option 2'
        
        # Select by visible text first option
        drop.select_by_visible_text("Option 1") 
        time.sleep(2)
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 1', 'Selected option should be Option 1'
        # Select by visible text second option
        drop.select_by_visible_text("Option 2")
        selected_option = drop.first_selected_option.text
        assert selected_option == 'Option 2', 'Selected option should be Option 2'
        time.sleep(2)
        self.driver.back()
