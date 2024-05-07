from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = browser.find_element(By.ID,"num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sumnum = str(int(num1)+int(num2))
    print(sumnum,type(sumnum))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sumnum) # ищем элемент с текстом "Python"
    button = browser.find_element(By.TAG_NAME,"button")
    button.click()
finally:
    time.sleep(4)
    browser.quit()