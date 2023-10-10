import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Открытие Хрома с помощью драйвера
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
Snew = Service('C:/Users/nkryat/Desktop/Niko/mycode/autotests2023/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=Snew)
#Тело теста
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")
time.sleep(5)
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()
time.sleep(5)
alert = driver.switch_to.alert
alert_text = alert.text
text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
print(text)
driver.quit()