
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    var = browser.find_element(By.ID, "input_value").text
    y = calc(var)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    submit = browser.find_element(By.ID, "solve")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()