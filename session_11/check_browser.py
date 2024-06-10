from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Driver initialization
driver = webdriver.Chrome()
try:
    # Open python.org
    driver.get("https://www.python.org")
    print(driver.title)

    # Find websearch element by name or by ID
    # search_input = driver.find_element("name","q")
    # search_input = driver.find_element("id","id-search-field")
    # search_input = driver.find_element(By.ID,"id-search-field")
    search_input = driver.find_element(By.CLASS_NAME,"search-field")
    search_input.clear()

    # Enter search text
    search_input.send_keys("getting started with python")

    # Emulate press the Enter button
    search_input.send_keys(Keys.RETURN)
    
    print(driver.current_url)
    
    # Check if title containg certain word
    assert "Python" in driver.title
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