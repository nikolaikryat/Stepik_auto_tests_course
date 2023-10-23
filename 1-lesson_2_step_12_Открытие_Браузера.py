import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link_1 = "https://SunInJuly.github.io/execute_script.html"
link_2 = "https://suninjuly.github.io/text_input_task.html"
# Открытие Хрома с помощью драйвера
driver = webdriver.Chrome()
driver.get(link_1)
#Тело теста
driver.get(link_2)
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