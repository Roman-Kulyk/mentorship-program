from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Driver initialization
driver = webdriver.Chrome()

try:
    # Open webpage DuckDuckGo
    driver.get("https://duckduckgo.com")
    print(driver.title)

    # Find websearch element by name
    search_input = driver.find_element("name","q")

    # Enter search text
    search_input.send_keys("Selenium")

    # Emulaate press the Enter button
    search_input.send_keys(Keys.ENTER)
     
    # Provide somet time for page to be opened
    time.sleep(3)

    # Check if title containg certain word
    assert "Selenium" in driver.title
    # If assertion failed handle the error.
except AssertionError:
    print("Something went wrong with the title!!!")
    # If no errors were raised execute following line of code
else:
    print("Test passed successfully!")
finally:
    # Close browser after fininshing test
    driver.close()  
print("Browser window is closed!")