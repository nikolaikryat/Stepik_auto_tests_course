from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import unittest

class TestAbs(unittest.TestCase):
#Первый тест
    def test_abs1(self):
        Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests/chromedriver_win32/chromedriver.exe')
        browser = webdriver.Chrome(service=Snew)
        browser.get("http://suninjuly.github.io/registration1.html")

    #Код, который заполняет обязательные поля, отправляет заполненную форму
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("Ivanov.Ivan@mail.ru")
    #Кнопка подтверждения
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
    #Присваивание переменной текста
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
    #Ассерт текста
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Несовпадение ожидаемого результата с результатом на практике!")

#Второй тест
    def test_abs2(self):
        Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests/chromedriver_win32/chromedriver.exe')
        browser = webdriver.Chrome(service=Snew)
        browser.get("http://suninjuly.github.io/registration2.html")

    #Код, который заполняет обязательные поля, отправляет заполненную форму
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("Ivanov.Ivan@mail.ru")
    #Кнопка подтверждения
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
    #Присваивание переменной текста
        welcome_text_elt_2 = browser.find_element(By.TAG_NAME, "h1")
        welcome_text_2 = welcome_text_elt_2.text 
    #Ассерт текста
        self.assertEqual(welcome_text_2, "Congratulations! You have successfully registered!", "NESOVPADENIJE REZULTATA NA PRKTIKE!")

if __name__ == "__main__":
    unittest.main()