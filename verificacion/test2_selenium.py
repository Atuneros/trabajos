from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("@yahoo.com")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(5)
driver.close()