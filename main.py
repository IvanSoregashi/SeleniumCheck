import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PATH = 'C:/Program Files (x86)/chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('http://users.bugred.ru/')

search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys('test', Keys.RETURN)
'''try:
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.close()'''

result_page = driver.find_elements(By.CSS_SELECTOR, '.ajax_load_row>tr>td:first-child')
for cell in result_page:
    print(cell.text)

time.sleep(1)

driver.close()
