from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    variable = browser.find_element(By.ID, "input_value").text
    print(variable)
    y = calc(variable)
    print(y)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()






finally:
    time.sleep(4)
    browser.quit()