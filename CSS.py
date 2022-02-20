import sys
sys.path.append(r'c:\users\tcdin\appdata\local\programs\python\python38-32\lib\site-packages')
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
cwd = os.chdir(r'C:\Users\tcdin\Desktop\New Folder')
CustomerID = "75521080"
password = "blue99"
driver = webdriver.Chrome()
driver.get('https://banking.westpac.com.au/wbc/banking/handler?TAM_OP=login&segment=personal&logout=false')
customeridfield = driver.find_element_by_xpath('/html/body/div[3]/main/form/div[2]/div/div[1]/div[1]/fieldset/div/label[1]/input')
customeridfield.send_keys(CustomerID)
passwordfield = driver.find_element_by_xpath('/html/body/div[3]/main/form/div[2]/div/div[1]/div[1]/fieldset/div/label[2]/input')
passwordfield.send_keys(password)
driver.find_element_by_xpath('/html/body/div[3]/main/form/div[2]/div/div[1]/div[1]/button').click()
driver.implicitly_wait(10)
bumpsavings = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div/span[2]').text
WestpacChoiceYouth = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/div/span[2]').text
driver.find_element_by_xpath('/html/body/div[1]/header/div[1]/div[2]/ul/li[4]/a').click()
driver.close()
f = open("Westpac.txt", 'a')
#print("bumpersavings account is", bumpsavings, file=f)
#print("choice account is", WestpacChoiceYouth,file=f)
transformed_string=(bumpsavings.replace(",","")).replace("$","")
transformed_string1=(WestpacChoiceYouth.replace(",","")).replace("$","")
print(transformed_string,file=f)
print(transformed_string1,file=f)

f.close()



