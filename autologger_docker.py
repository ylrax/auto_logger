import sys
from os import environ
from base64 import b64decode
from time import sleep, localtime, strftime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


if len(sys.argv) == 1:
    print("No default argument passed!!")
    print("Using the environment variables")
    print(sys.version)
    param_1 = environ.get("USER", 'dXNlcm5hbWU=')
    param_2 = environ.get("PASS", 'MTIzNDU2')

else:
    param_1 = sys.argv[1]
    param_2 = sys.argv[2]

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


print("Opening the web: ", strftime("%m/%d/%Y, %H:%M:%S", localtime()))
driver.get('https://www.minijuegos.com/')

sleep(25)

print("Handle cookie banner...")
try:
    print("  First option")
    cookie = driver.find_element(by=By.XPATH, value='//*[@id="qc-cmp2-ui"]/div[3]/div/button[2]')
    cookie.click()
except NoSuchElementException:
    try:
        print("  Second option")
        cookie = driver.find_element(by=By.XPATH, value='//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        cookie.click()
    except NoSuchElementException:
        print("  No XPATH option?")
        cookie = driver.find_element(by=By.CLASS_NAME, value='css-52n1sd')
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

if param_1 == 'dXNlcm5hbWU=':
    print("Using default user (not real)")

driver.find_element(by=By.XPATH, value="//*[@id='login-uid']").send_keys(b64decode(param_1.encode('ascii')).decode('utf-8')) # 'dXNlcm5hbWU='
driver.find_element(by=By.XPATH, value="//*[@id='login-pwd']").send_keys(b64decode(param_2.encode('ascii')).decode('utf-8')) # 'MTIzNDU2'
driver.find_element(by=By.XPATH, value="//*[@id='login-pwd']").send_keys(webdriver.common.keys.Keys.ENTER)


print("Inside of profile?!!!")
sleep(15)
#screenshot = driver.save_screenshot('login3.png')
print("Ciao!!")

driver.quit()
