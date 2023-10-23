from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import math

link = "https://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
field = browser.find_element(By.CSS_SELECTOR, "#answer")
field.send_keys(y)

checkbox_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

radiobutton_1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
button.click()    

time.sleep(10)
browser.quit()