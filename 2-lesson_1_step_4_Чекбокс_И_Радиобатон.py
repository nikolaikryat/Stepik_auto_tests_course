from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=Snew)
browser.get("https://suninjuly.github.io/math.html")

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