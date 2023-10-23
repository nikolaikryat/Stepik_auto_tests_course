from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
    #Открытие браузера
Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=Snew)
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys("Petrov")
input3 = browser.find_element(By.NAME, "email")
input3.send_keys("Smolensk@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'XXX.txt') 
element = browser.find_element(By.CSS_SELECTOR, "#file")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

time.sleep(10)