from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
    return math.log(abs(12*math.sin(int(x))))
    #Открытие браузера
Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=Snew)
browser.get("http://suninjuly.github.io/alert_accept.html")

button_journey = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
    #Принятие всплывающего окна
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
field = browser.find_element(By.CSS_SELECTOR, "#answer")
field.send_keys(y)

button_2 = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

time.sleep(5)


