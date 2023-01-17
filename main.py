import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_base import *

PATH = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(service=Service(PATH))

US = UsersBugred(driver)

for cell in US.search_email('test'):
    print(cell.text)

time.sleep(1)

driver.close()
