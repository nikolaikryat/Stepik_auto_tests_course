from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import math
import re

try:
        #Формула после покупки
    def calc(x):
        return math.log(abs(12*math.sin(int(x))))

        #Открырие браузера
    Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
    browser = webdriver.Chrome(service=Snew)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

        #Говорим Selenium проверять значение цены 15 секунд, пока кнопка не станет кликабельной
    Lake_house = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
        #нажатие на кнопку "Book" 
    message = browser.find_element(By.CSS_SELECTOR, "#book").click()

        #Расчет формулы и забивание ответа в поле ввода
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)

        #Скролл вниз
    button_2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    button_2.click()

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