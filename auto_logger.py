import sys
from os import name as os_name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, localtime, strftime
from base64 import b64decode
from pyvirtualdisplay import Display

if len(sys.argv) == 1:
    print("No argument passed!!")
    sys.exit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")

if os_name == "posix":
    display = Display(visible=0, size=(1200, 800))
    display.start()
    driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',
                              chrome_options=chrome_options)
else:
    driver = webdriver.Chrome(chrome_options=chrome_options)


# driver.add_argument(“ — incognito”)
print("Opening the web")
print(strftime("%m/%d/%Y, %H:%M:%S", localtime()))
driver.get('https://www.minijuegos.com/')

sleep(36)

print("Handle cookie banner")
cookie = driver.find_element_by_class_name("css-52n1sd")
cookie.click()
sleep(6)

print("Logging stage")
# driver.find_element_by_class_name('banner_accept--X').click()
try:
    log = driver.find_element_by_id("user-widget-no-logged")
    log.click()
except NoSuchElementException:
    print("Element not found. Waiting")
    sleep(30)
    log = driver.find_element_by_id("user-widget-no-logged")
    log.click()

sleep(2)
print("Inserting logging values")
driver.find_element_by_xpath("//*[@id='login-uid']").send_keys(b64decode(sys.argv[1].encode('ascii')).decode('utf-8')) # 'dXNlcm5hbWU='
driver.find_element_by_xpath("//*[@id='login-pwd']").send_keys(b64decode(sys.argv[2].encode('ascii')).decode('utf-8')) # 'MTIzNDU2'
driver.find_element_by_xpath("//*[@id='login-pwd']").send_keys(webdriver.common.keys.Keys.ENTER) # webdriver.common.keys.Keys.ENTER?

print("Inside of profile?!!!")
sleep(15)
print("Ciao!!")

driver.quit()
if os_name == "posix":
    display.stop()
