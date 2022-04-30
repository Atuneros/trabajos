from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# 1

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(1)

# 2

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("aaaa")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(1)

# 3

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("aaaa@aaa.com")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(1)

# 4

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("@yahoo.com")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(1)

# 5

driver.get("http://automationpractice.com/")

print(driver.title)

email_field = driver.find_element_by_name("email")

email_field.clear()
email_field.send_keys("<script>alert('hola')</script>")
email_field.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(1)

driver.close()