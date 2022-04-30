from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/")

print(driver.title)

search_bar = driver.find_element_by_name("search_query")

search_bar.clear()
search_bar.send_keys("camiseta")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)

time.sleep(5)
driver.close()