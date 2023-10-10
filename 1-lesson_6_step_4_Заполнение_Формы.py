import time

import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    #Открытие Хрома с помощью драйвера
    Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=Snew)
    driver.maximize_window()
    driver.get(link)
    #Манимуляции с полями
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR, "#submit_button")
    button.click()
    time.sleep(5)
finally:
    alert = driver.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    print(text)
    driver.quit()