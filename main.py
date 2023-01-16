import time

from selenium import webdriver
from selenium_base import *

PATH = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
TEST_SITE = 'http://users.bugred.ru/'

SB = SeleniumBase(driver)

SB.driver.get(TEST_SITE)

for cell in result_page:
    print(cell.text)

time.sleep(1)

driver.close()
