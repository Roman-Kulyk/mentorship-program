from selenium import webdriver
# TRADITIONAL LOCATORS
# class name - Locates elements whose class contains the search value (compound
# class names are not permitted).
driver = webdriver.Chrome()
driver.find_element(By.CLASS_NAME, "information")

# css selector - Locates elements matching CSS selector.
driver = webdriver.Chrome()
driver.find_element(By.CSS_SELECTOR, "#fname")

# id - Locates elements whose ID attribute matches the search value.
driver = webdriver.Chrome()
driver.find_element(By.ID, "lname")

# name - Locates elements whose NAME attribute matches the search value.
driver = webdriver.Chrome()
driver.find_element(By.NAME, "newsletter")

# link text - Locates elements whose visible text matches the search value.
driver = webdriver.Chrome()
driver.find_element(By.LINK_TEXT, "Selenium Official Page")
                    
# partial link text - Locates anchor elements whose visible text contains the
# seearch value. If multiple elements are matching, only the first one will be
# selected.
driver = webdriver.Chrome()
driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
                    


# tag name - Locates elements whose tag matches the search value.
driver = webdriver.Chrome()
driver.find_element(By.TAG_NAME, "a")

# xpath - Locates elements matching an XPath expression.
driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//input[@value='f']")


# RELATIVE LOCATORS
# Above
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
# Below
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID:"email"})

# Left of
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})

# Right of
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})

# Near
email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})