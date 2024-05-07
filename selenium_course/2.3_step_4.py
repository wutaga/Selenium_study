from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options)
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element(By.CSS_SELECTOR,"button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = browser.find_element(By.ID,"input_value").text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally:
    time.sleep(5)
    browser.quit()
