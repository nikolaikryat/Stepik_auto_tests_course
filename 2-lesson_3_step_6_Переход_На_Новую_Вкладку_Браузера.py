from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import math

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    def calc(x):
        return math.log(abs(12*math.sin(int(x))))
        #Открытие браузера
    Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
    browser = webdriver.Chrome(service=Snew)
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
        #Перехлд на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)

    button_2 = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

        #Печатает из всплывайки число
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    print(text)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()