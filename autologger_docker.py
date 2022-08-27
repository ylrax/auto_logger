import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep, localtime, strftime
from base64 import b64decode

if len(sys.argv) == 1:
    print("No argument passed!!")
    sys.exit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-dev-shm-usage')    

driver = webdriver.Chrome(options=chrome_options)


# driver.add_argument(“ — incognito”)
print("Opening the web: ", strftime("%m/%d/%Y, %H:%M:%S", localtime()))
driver.get('https://www.minijuegos.com/')

sleep(9)

print("Handle cookie banner...")
cookie = driver.find_element(by=By.XPATH, value='//*[@id="qc-cmp2-ui"]/div[3]/div/button[2]')
cookie.click()
sleep(6)
#screenshot = driver.save_screenshot('entered.png')

print("Logging stage...")
# driver.find_element_by_class_name('banner_accept--X').click()
try:
    log = driver.find_element(by=By.ID, value="user-widget-no-logged")
    log.click()
except NoSuchElementException:
    print("Element not found. Waiting")
    sleep(30)
    log = driver.find_element(by=By.ID, value="user-widget-no-logged")
    log.click()

sleep(2)
print("Inserting logging values")

if sys.argv[1] == 'dXNlcm5hbWU=':
    print("Using default user (not real)")

driver.find_element(by=By.XPATH, value="//*[@id='login-uid']").send_keys(b64decode(sys.argv[1].encode('ascii')).decode('utf-8')) # 'dXNlcm5hbWU='
driver.find_element(by=By.XPATH, value="//*[@id='login-pwd']").send_keys(b64decode(sys.argv[2].encode('ascii')).decode('utf-8')) # 'MTIzNDU2'
driver.find_element(by=By.XPATH, value="//*[@id='login-pwd']").send_keys(webdriver.common.keys.Keys.ENTER)


print("Inside of profile?!!!")
sleep(15)
#screenshot = driver.save_screenshot('login3.png')
print("Ciao!!")

driver.quit()
