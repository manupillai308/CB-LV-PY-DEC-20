from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get("https://www.google.com")
time.sleep(3)

textbox = browser.find_element_by_name("q")
textbox.send_keys("What is the age of Modi?" + Keys.ENTER)
# textbox.send_keys(Keys.ENTER)
time.sleep(5)



# button = browser.find_element_by_name("btnK")
# button.click()
# time.sleep(3)
# browser.close()