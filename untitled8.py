import sys
sys.path.append(r'c:\users\tcdin\appdata\local\programs\python\python38-32\lib\site-packages')
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
driver.get('https://mail.google.com/mail/u/0/#inbox')
username = "tdarpitha2004@gmail.com"
password = "platiumred998"
usernamefield = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
usernamefield.send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

passwordfield = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
passwordfield.send_keys(password)
nextpage= driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
#driver.implicitly_wait(10)
driver.close()
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.close()

/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input
/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span