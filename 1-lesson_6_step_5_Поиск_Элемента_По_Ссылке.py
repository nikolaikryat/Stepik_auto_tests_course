import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=Snew)
browser.maximize_window()
browser.get("http://suninjuly.github.io/find_link_text")
    #Если хотим найти элемент по полному соответствию текста
link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
    #Если хотим найти элемент со ссылкой по подстроке
    #link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
    #link.click()
time.sleep(1)
input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()