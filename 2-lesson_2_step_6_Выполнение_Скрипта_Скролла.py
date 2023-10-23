from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import math
import re

link = "https://SunInJuly.github.io/execute_script.html"
    #Формула
def calc(x):
    return math.log(abs(12*math.sin(int(x))))
    #Открытие браузера
browser = webdriver.Chrome()
browser.get(link)
    #Определение икса и внесение его в поле ввода
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
print(x)
y = calc(x)
field = browser.find_element(By.CSS_SELECTOR, "#answer")
field.send_keys(y)
    #Заполнение чекбокса
checkbox_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    #Выбор радиобатона
radiobutton_1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_1)
radiobutton_1.click()
    #Поиск кнопки сабмит и нажатие
button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    #Пауза 10 секунд перед выходом
time.sleep(10)