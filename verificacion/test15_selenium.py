from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

print(driver.title)

email_create = driver.find_element_by_name("email_create")

email_create.clear()
email_create.send_keys("aaaaa@aaaaa.com")
email_create.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(5)
driver.close()