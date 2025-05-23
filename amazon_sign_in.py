from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
sleep(2)
#Logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']" )
#email field
driver.find_element(By.ID, "ap_email")
#Continue button
driver.find_element(By.ID, "continue")
#Conditions Link
driver.find_element(By.LINK_TEXT, "Conditions of Use")
#Privacy Link
driver.find_element(By.LINK_TEXT, "Privacy Notice")
#Need help link or button
driver.find_element(By.LINK_TEXT, "Need help?").click()
#Forgot Password link
sleep(2)
driver.find_element(By.LINK_TEXT, "Forgot your password?")

driver.find_element(By.LINK_TEXT, "Other issues with Sign-In")

driver.find_element(By.ID, "createAccountSubmit")