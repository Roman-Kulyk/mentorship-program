from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Driver initialization
driver = webdriver.Chrome()

try:
    # Open webpage DuckDuckGo
    driver.get("https://duckduckgo.com")

    # Find websearch element by name
    search_input = driver.find_element("name","q")

    # Enter search text
    search_input.send_keys("Selenium")

    # Emulaate press the Enter button
    search_input.send_keys(Keys.ENTER)
     
    # Provide somet time for page to be opened
    time.sleep(3)

    # Check if title containg word "Selenium"
    
    assert "Selenium" in driver.title
finally:

    # Close browser after fininshing test
    driver.quit()
print("Test passed successfully!")