from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from unidecode import unidecode
from selenium.webdriver.common.keys import Keys
import pandas as pd
from collections import defaultdict
import json
from datetime import datetime

driver = webdriver.Chrome('/Users/ik/Codes/chinese_immigrants/webdriver/chromedriver')

WAIT_TIME = 30
SUBJ_WORD = "cricket"
NPAGES = 15000

# base URL
BASE_URL = "https://www.google.com.au"

driver.get(BASE_URL)

WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.XPATH, "//input[@id='lst-ib']"))).send_keys(SUBJ_WORD)
driver.find_element_by_xpath("//input[@type='submit']").click()
WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "News"))).click()

dc = []

for p in range(1, NPAGES + 1):	

	for d in driver.find_elements_by_xpath("//div[contains(@class, 'card-section')]"):
		try:
			aas = d.find_elements_by_xpath(".//a")
			if len(aas) == 1:
				hdl = aas[-1].text.strip()
				if len(hdl.split()) > 2:
					src = " ".join([w.text.strip() for w in d.find_elements_by_xpath(".//span")]).split("-")[0]
				dc.append({"headline": hdl, "source": src})
		except:
			pass

	for h3 in driver.find_elements_by_xpath("//h3"):
		hdl = h3.find_element_by_xpath(".//a").text.strip()
		scr = h3.find_element_by_xpath(".//following-sibling::div")
		src_txt = scr.text.strip().split("-")[0]
		abst = scr.find_element_by_xpath(".//following-sibling::div").text.strip()
		dc.append({"headline": hdl,
					"preview": abst,
					"source": src_txt})

	if p%10 == 0:
		print("page: {}, headlines collected: {}".format(p, len(dc)))

	driver.find_element_by_xpath("//a[@id='pnnext']").send_keys(Keys.RETURN)

driver.quit()

right_now = datetime.now()
tm_stamp = "{:02d}{:02d}{:02d}".format(right_now.day, right_now.month, right_now.year)
json.dump(dc, open("-".join(["googlenews", str(len(dc)), "hdl", SUBJ_WORD, tm_stamp]) + ".json", "w"))


	
	




