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

for d in driver.find_elements_by_xpath("//div[contains(@class, 'card-section')]"):
	aas = d.find_elements_by_xpath(".//a")
	if len(aas) == 1:
		hdl = aas[-1].text.strip()
		if len(hdl.split()) > 2:
			print(hdl)
			src = " ".join([w.text.strip() for w in d.find_elements_by_xpath(".//span")])
			print(src)
for h3 in driver.find_elements_by_xpath("//h3"):
	hdl = h3.find_element_by_xpath(".//a").text.strip()
	print(hdl)
	src = h3.find_element_by_xpath(".//following-sibling::div").text.strip()
	print(src)
	#abst = d.find_element_by_xpath(".//div[@class='st']").text.strip()
	
	#print(d.text.strip())
	#print("--- abstract:", abst)
	#print("--- source:", src)




