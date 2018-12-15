import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from base64 import b64decode

if len(sys.argv) == 1:
    print("No argument passed!!")
	sys.exit()

driver = webdriver.Chrome()
# driver.add_argument(“ — incognito”)
print("Opening the web")
driver.get('https://www.minijuegos.com/')

sleep(5) 
print("Logging stage")
log = driver.find_element_by_id("user-widget-no-logged")	
log.click()

sleep(2)
print("Inserting logging values")
driver.find_element_by_xpath("//*[@id='login-uid']").send_keys(b64decode(sys.argv[1].encode('ascii')).decode('utf-8')) # 'dXNlcm5hbWU='
driver.find_element_by_xpath("//*[@id='login-pwd']").send_keys(b64decode(sys.argv[2].encode('ascii')).decode('utf-8')) # 'MTIzNDU2'
driver.find_element_by_xpath("//*[@id='login-pwd']").send_keys(webdriver.common.keys.Keys.ENTER) # webdriver.common.keys.Keys.ENTER?

print("Inside of profile?!!!")
sleep(4)
print("Ciao!!")

driver.quit()
