from selenium import webdriver
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

driver.get('https://www.minijuegos.com/')
screenshot = driver.save_screenshot('test.png')
driver.quit()

print("Done!")
