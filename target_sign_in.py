from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 3 As: Arrange / Act / Assert

# Arrange (setup)
# init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')
sleep(3)

#Find and click buttons
driver.find_element(By.ID, "account-sign-in").click()
sleep(2)
driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").click()
sleep(2)
driver.find_element(By.XPATH, "//*[text()='Sign in or create account']")
