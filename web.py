from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path=r'./phantomjs')
driver.get("https://www.baidu.com")
driver.save_screenshot("baidu.png")
time.sleep(3)

driver.find_element_by_id("kw").send_keys("hello")
driver.save_screenshot("baidu2.png")

driver.find_element_by_id("kw").send_keys(Keys.RETURN)
time.sleep(2)
driver.save_screenshot("baidu3.png")
