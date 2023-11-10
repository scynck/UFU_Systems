from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import glob
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome() 
'''options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"download.default_directory": r"C:\Data_Files\output_files"})
s = Service('C:\\BrowserDrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
'''

driver.get("https://sg.ufu.br/")

login = driver.find_element(By.NAME, "login")
login.send_keys("rafael.mjas")
password = driver.find_element(By.NAME, "password")
password.send_keys("DonaSida1")
button = driver.find_element(By.CLASS_NAME, "blue.medium").click()
arvore = driver.find_element(By.ID, "tree")
print(arvore.text)
app = driver.find_element(By.NAME, "treeFilterText")
app.send_keys("11.02.02.99.01")
app.send_keys(Keys.ENTER)
input("Digite enter para sair")



#arvore1 = arvore.find_elements(By.TAG_NAME, "li")
'''arvore1 = arvore.find_elements(By.XPATH, "//*[@id='361']")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Educação')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Controle')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cadastro do Aluno')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11.02.02.99')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11.02.02.99.01')]"))).click()'''

matricula = driver.find_element(By.ID, "matricula")
matricula.send_keys("Rafael Monteiro")
#button1 = driver.find_element(By.CLASS_NAME, "red").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/table/tbody/tr/td[3]/button"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr/td[1]/input"))).click()
#PDF 
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[2]/button[1]"))).click()
#Excel
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[2]/button[2]"))).click()



home = os.path.expanduser("~")
downloadspath=os.path.join(home, "Downloads")
downloadspath = 'C:\\Users\Administrador\Downloads'
list_of_files = glob.glob(downloadspath+"\*.xlsx") # * means all if need specific format then *.csv
list_of_files_init = list_of_files
print(len(list_of_files))
while(len(list_of_files) == len(list_of_files_init)):
    time.sleep(1)
    print(len(list_of_files))
    print(len(list_of_files_init))
    list_of_files = glob.glob(downloadspath+"\*.xlsx") # * means all if need specific format then *.csv
    
latest_file = max(list_of_files, key=os.path.getctime)

print(latest_file)


df = pd.read_excel(latest_file)
print(df)

input("Digite enter para sair")

driver.quit()
