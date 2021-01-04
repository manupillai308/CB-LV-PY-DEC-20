from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get("https://www.youtube.com")
# browser.save_screenshot("./screenshot1.jpg")
time.sleep(3)

html = browser.page_source
#beautiful soup code
open("./home.html", "w", encoding="utf-8").write(html)
# browser.save_screenshot("./screenshot2.jpg")
# time.sleep(2)
browser.close()


# button = browser.find_element_by_name("btnK")
# button.click()
# time.sleep(3)
# browser.close()