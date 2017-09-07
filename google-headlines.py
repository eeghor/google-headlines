from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from unidecode import unidecode
import pandas as pd

driver = webdriver.Chrome('/Users/ik/Codes/chinese_immigrants/webdriver/chromedriver')

WAIT_TIME = 30
# base URL
BASE_URL = "https://www.google.com.au"

driver.get(BASE_URL)

WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, "//input[@id='lst-ib']"))).send_keys("cricket")
driver.find_element_by_xpath("//input[@type='submit']").click()
WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "News"))).click()

for d in driver.find_elements_by_xpath("//div[contains(@class, 'Js')]"):
	print(d.text)




