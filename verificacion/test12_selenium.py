from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/index.php?id_category=5&controller=category")

print(driver.title)

driver.find_element_by_class_name("product_img_link").click()

print(driver.current_url)

time.sleep(5)
driver.close()