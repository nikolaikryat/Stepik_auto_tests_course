from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
treasure_valuex = treasure.get_attribute("valuex")
y = calc(treasure_valuex)
field = browser.find_element(By.CSS_SELECTOR, "#answer")
field.send_keys(y)

checkbox_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

radiobutton_1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
time.sleep(2)


button = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
button.click()    

time.sleep(5)
browser.quit()