from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="C:/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)

lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")
while (cookie):
    cookie.click()


time.sleep(10)

driver.quit()
