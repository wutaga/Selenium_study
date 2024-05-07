from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    pic = browser.find_element(By.ID, "treasure")
    pic_x = pic.get_attribute("valuex")
    print(pic_x)
    y = calc(pic_x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    time.sleep(2)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    time.sleep(2)
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()