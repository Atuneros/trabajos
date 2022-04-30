from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/index.php?id_product=1&controller=product")

print(driver.title)

wishlist_button = driver.find_element_by_id("wishlist_button").click()

print(driver.current_url)

time.sleep(5)
driver.close()