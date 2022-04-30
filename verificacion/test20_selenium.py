from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

block_top_menu = driver.find_element_by_id("block_top_menu")
sf_with_ul = block_top_menu.find_element_by_class_name("sf-with-ul")

hover = ActionChains(driver).move_to_element(sf_with_ul)
hover.perform()

time.sleep(5)
driver.close()