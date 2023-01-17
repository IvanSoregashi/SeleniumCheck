from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 5, 0.2)

    def visible_element(self, locator):
        '''Waiting on element and return WebElement if it is visible'''
        return self.__wait.until(ec.visibility_of_element_located(locator))

    def visible_elements(self, locator):
        '''Waiting on elements and return List(WebElement) if it is visible'''
        return self.__wait.until(ec.visibility_of_all_elements_located(locator))


class UsersBugred(SeleniumBase):
    _URI = 'http://users.bugred.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self._URI)

    def search(self, query):
        search_bar = self.visible_element((By.NAME, 'q'))
        search_bar.send_keys(query, Keys.RETURN)
        return self.visible_elements((By.CSS_SELECTOR, '.ajax_load_row>tr>td:first-child'))
