from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

header = driver.find_element_by_id("header")
banner = header.find_element_by_class_name("banner")
container = banner.find_element_by_class_name("container")
row = container.find_element_by_class_name("row")
row.find_element_by_tag_name("a").click()

print(driver.current_url)

time.sleep(5)
driver.close()