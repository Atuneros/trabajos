from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

print(email_field)

time.sleep(5)
driver.close()
