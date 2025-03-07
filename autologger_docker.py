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
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


print("Opening the web: ", strftime("%m/%d/%Y, %H:%M:%S", localtime()))
driver.get('https://www.minijuegos.com/')

sleep(20)

def check_exists_by_xpath(xpath, source=By.XPATH):
    try:
        driver.find_element(by=source, value=xpath)
    except NoSuchElementException:
        return False
    return True

print("Check all cookie existence")
print("General banner: ", check_exists_by_xpath('//*[@id="qc-cmp2-ui"]'))
print("General banner: ", check_exists_by_xpath('qc-cmp2-ui', By.ID))
print("Button banner: ", check_exists_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))
print("Botton banner: ", check_exists_by_xpath(' css-52n1sd', By.CSS_SELECTOR))
print("Botton banner: ", check_exists_by_xpath(' css-52n1sd', By.CLASS_NAME))
print("log banner: ", check_exists_by_xpath("user-widget-no-logged", By.ID))
print("log2 banner: ", check_exists_by_xpath('//*[@id="user-widget-no-logged"]/li/span'))
print("log3 banner: ", check_exists_by_xpath('//*[@id="user-widget-no-logged"]'))

sleep(4)
# https://stackoverflow.com/questions/73199578/issue-when-running-python-script-with-selenium-over-gcp-cloud-run
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#WebDriverWait(driver, 140).until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]')))

print("Handle cookie banner...")
try:
    print("***  First option")
    cookie = driver.find_element(by=By.XPATH, value='//*[@id="qc-cmp2-ui"]/div[3]/div/button[2]')
    cookie.click()
except NoSuchElementException:
    try:
        print("***  Second option")
        sleep(2)
        cookie = driver.find_element(by=By.XPATH, value='//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        cookie.click()
    except NoSuchElementException:
        print("***  No XPATH option?")
        sleep(2)


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
