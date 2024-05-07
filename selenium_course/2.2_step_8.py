from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'text.txt')
print(file_path)
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Илья")
    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Иванов")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@mail.ru")
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(6)
    browser.quit()
