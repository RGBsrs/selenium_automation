import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import xlsxwriter

load_dotenv()

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://itdashboard.gov/")
dive_button = driver.find_element(By.LINK_TEXT, value='DIVE IN')
dive_button.click()

amounts = driver.find_elements(By.XPATH, '//*[@id="agency-tiles-widget"]/div/div[*]/div[*]/div/div/div/div[1]/a/span[2]')

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet(name='Agencies')
row = 0
col = 0

for amount in amounts:
    worksheet.write(row, col, amount.text)
    row = row + 1
workbook.close()
try:
    agency = driver.find_element(By.PARTIAL_LINK_TEXT, os.getenv("AGENCY"))
    agency.click()
except Exception as e:
    print('Some error\n')
    print(e)

driver.close()

