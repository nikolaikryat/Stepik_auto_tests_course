from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

try: 
    Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
    browser = webdriver.Chrome(service=Snew)
    browser.get("http://suninjuly.github.io/registration2.html")

    # Ваш код, который заполняет обязательные поля
    inputFN = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
    inputFN.send_keys("Ivan")
    inputLN = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
    inputLN.send_keys("Ivanov")
    inputEMail = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
    inputEMail.send_keys("Ivanov.Ivan@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()