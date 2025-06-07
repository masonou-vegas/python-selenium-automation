from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
#driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&showRememberMe=true&openid.pape.max_auth_age=0&pageId=usflex&prepopulatedLoginId=&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&policy_handle=Retail-Checkout')
sleep(2)

#locate elements
#Logo
driver.find_element(By.XPATH, "//*[@class='a-icon a-icon-logo']" )
#Create account
driver.find_element(By.XPATH, '//*[@class="a-spacing-small"]')
#name
driver.find_element(By.ID, "ap_customer_name")
#email
driver.find_element(By.ID, "ap_email")
#password
driver.find_element(By.ID, "ap_password")
# re enter password
driver.find_element(By.ID, "ap_password_check")
#verify email button
driver.find_element(By.ID, "continue")
#conditions of use
driver.find_element(By.LINK_TEXT, "Conditions of Use")
#privacy notice
driver.find_element(By.LINK_TEXT, "Privacy Notice")
#sign in link
driver.find_element(By.ID, "ra-sign-in-link")