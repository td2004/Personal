import sys
sys.path.append(r'c:\users\tcdin\appdata\local\programs\python\python38-32\lib\site-packages')
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#browser = webdriver.chrome
driver = webdriver.Chrome()
driver.get('https://www.westpac.com.au/')
driver.find_element_by_id(“ID”).send_keys(“username”)
driver.find_element_by_id (“ID”).send_keys(“password”)
driver.find_element_by_id(“submit”).click()

