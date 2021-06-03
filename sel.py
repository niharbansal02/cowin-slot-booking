from os import name, path
import os
from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def repeater(func):
	while True:
		try:
			retVal = func()
			break
		except:
			continue
	
	return retVal

# //body/app-root[1]/ion-app[1]/ion-router-outlet[1]/app-beneficiary-dashboard[1]/ion-content[1]/div[1]/div[1]/ion-grid[1]/ion-row[1]/ion-col[1]/ion-grid[1]/ion-row[2]/ion-col[1]/ion-grid[1]/ion-row[4]/ion-col[2]/ul[1]/li[1]/a[1]
def getOTP(startTime):
	while True:
		os.system("adb shell content query --uri content://sms --projection _id,address,body,read,date,type,time > sms.txt")
		fh = open("sms.txt")
		data = fh.read()
		try:
			msgTime = int(data.split("_id=")[1].split("time=")[1].split("\n")[0])
		except: continue

		if(msgTime > startTime * 1000):
			print(msgTime, startTime)
			try:
				otp = data.split("_id=")[1].split("CoWIN is ")[1].split(".")[0]
			except:
				continue
			print("\033[1;32m", otp, "\033[0m")
			return otp
		fh.close()


def startTheShow():
	startTimeShow = time.time()
	browser = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")
	browser.maximize_window()
	browser.delete_all_cookies()
	repeater(lambda: browser.get("https://selfregistration.cowin.gov.in/"))
	repeater(lambda: browser.find_element_by_id("mat-input-0").send_keys("8989788395"))

	startTime = int(time.time())
	repeater(lambda: browser.find_element_by_class_name("covid-button-desktop").click())
	# time.sleep(0.2)
	otp = getOTP(startTime)
	# otp = int(input("Enter OTP: "))
	repeater(lambda: browser.find_element_by_id("mat-input-1").send_keys(otp))
	repeater(lambda: browser.find_element_by_class_name("next-btn").click())
	# time.sleep(5)
	sparsh = "//body/app-root[1]/ion-app[1]/ion-router-outlet[1]/app-beneficiary-dashboard[1]/ion-content[1]/div[1]/div[1]/ion-grid[1]/ion-row[1]/ion-col[1]/ion-grid[1]/ion-row[2]/ion-col[1]/ion-grid[1]/ion-row[4]/ion-col[2]/ul[1]/li[1]/a[1]"
	nihar = "//body/app-root[1]/ion-app[1]/ion-router-outlet[1]/app-beneficiary-dashboard[1]/ion-content[1]/div[1]/div[1]/ion-grid[1]/ion-row[1]/ion-col[1]/ion-grid[1]/ion-row[3]/ion-col[1]/ion-grid[1]/ion-row[4]/ion-col[2]/ul[1]/li[1]/a[1]"
	repeater(lambda: browser.find_element_by_xpath(sparsh).click())
	# time.sleep(1)
	repeater(lambda: browser.find_element_by_class_name("mat-input-element").send_keys(457001))
		
	searchCnt = 0
	while True:
		timeNow = time.time()
		if(timeNow - startTimeShow >= 300):
			browser.quit()
			break
		try:
			time.sleep(1)
			repeater(lambda: browser.find_element_by_class_name("pin-search-btn").click())
			repeater(lambda: browser.find_element_by_class_name("form-check").click())
			searchCnt += 1
			print(searchCnt)
			rowNums = range(1, 7)
			colNums = range(1, 4)
			
			for colNum in colNums:
				for rowNum in rowNums:
					xPath = "//body/app-root[1]/ion-app[1]/ion-router-outlet[1]/app-appointment-table[1]/ion-content[1]/div[1]/div[1]/ion-grid[1]/ion-row[1]/ion-grid[1]/ion-row[1]/ion-col[1]/ion-grid[1]/ion-row[1]/ion-col[2]/form[1]/ion-grid[1]/ion-row[3]/ion-col[3]/div[1]/div[1]/mat-selection-list[1]/div[" + str(rowNum) + "]/mat-list-option[1]/div[1]/div[2]/ion-row[1]/ion-col[2]/ul[1]/li[" + str(colNum) + "]/div[1]/div[1]/a[1]"
					# time.sleep(2)
					try:
						# ele = repeater(lambda: browser.find_element_by_xpath(xPath))
						ele = browser.find_element_by_xpath(xPath)
						txt = ele.text
						print(txt)
					except:
						# ele = repeater(lambda: browser.find_element_by_xpath(xPath))
						# ele = browser.find_element_by_xpath(xPath)
						print("\033[1;31mELEMET\033[0m")
						pass
					finally:
						# txt = lambda: ele.text
						# print(txt)
						pass
					try:
						if(int(txt) > 0):
							ele.click()
							repeater(lambda: browser.find_element_by_xpath("//*[contains(text(), '06:00')]")).click()
							# browser.find_element_by_link_text("Welcome Everyone").send_keys(Keys.NULL)

					except:
						# print("No num")
						pass
		except KeyboardInterrupt:
			browser.quit()


if __name__ == "__main__":
	while True:
		startTheShow()
		print("\033[1;34mNext\033[0m")
		# getOTP(11)
		# pass
