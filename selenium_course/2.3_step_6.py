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
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR,"button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(4)
    browser.quit()
