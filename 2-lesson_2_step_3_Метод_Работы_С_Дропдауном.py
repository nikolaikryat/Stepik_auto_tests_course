from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
def sum(x, y):
    return str(int(x) + int(y))

Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=Snew)
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
x = x_element.text
y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
y = y_element.text
z = sum(x, y)
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(z)

button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()  

time.sleep(10)

