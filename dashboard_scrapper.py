from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://itdashboard.gov/")
dive_button = driver.find_element(By.LINK_TEXT, value='DIVE IN')
dive_button.click()



amounts = driver.find_elements(By.XPATH, '//*[@id="agency-tiles-widget"]/div/div[*]/div[*]/div/div/div/div[1]/a/span[2]')
for amount in amounts:
    print(amount.text)
driver.close()