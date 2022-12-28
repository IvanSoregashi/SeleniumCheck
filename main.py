import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PATH = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(PATH)
TEST_SITE = 'http://users.bugred.ru/'


class SelenuimBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 5, 0.2)

    def visible_element(self, locator):
        '''Waiting on element and return WebElement if it is visible'''
        return self.__wait.until(ec.visibility_of_element_located(locator))

    def visible_elements(self, locator):
        '''Waiting on elements and return List(WebElement) if it is visible'''
        return self.__wait.until(ec.visibility_of_all_elements_located(locator))


SB = SelenuimBase(driver)

SB.driver.get(TEST_SITE)

search_bar = SB.visible_element((By.NAME, 'q'))
search_bar.send_keys('test', Keys.RETURN)
result_page = SB.visible_elements((By.CSS_SELECTOR, '.ajax_load_row>tr>td:first-child'))

for cell in result_page:
    print(cell.text)

time.sleep(1)

driver.close()
