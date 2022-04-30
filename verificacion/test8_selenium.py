from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

social_block = driver.find_element_by_id("social_block")
social_block.find_element_by_class_name("twitter").click()

print(driver.current_url)

time.sleep(5)
driver.close()