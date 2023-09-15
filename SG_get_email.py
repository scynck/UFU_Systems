from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome() 

driver.get("https://sg.ufu.br/")

login = driver.find_element(By.NAME, "login")
login.send_keys("rafael.mjas")
password = driver.find_element(By.NAME, "password")
password.send_keys("DonaSida1")
button = driver.find_element(By.CLASS_NAME, "blue.medium").click()
arvore = driver.find_element(By.ID, "tree")
print(arvore.text)
#arvore1 = arvore.find_elements(By.TAG_NAME, "li")
arvore1 = arvore.find_elements(By.XPATH, "//*[@id='361']")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Educação')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Controle')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Cadastro do Aluno')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11.02.02.99')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '11.02.02.99.01')]"))).click()
matricula = driver.find_element(By.ID, "matricula")
matricula.send_keys("Rafael Monteiro")
#button1 = driver.find_element(By.CLASS_NAME, "red").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/table/tbody/tr/td[3]/button"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr/td[1]/input"))).click()
#PDF 
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[2]/button[1]"))).click()
#Excel
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div[3]/div[2]/div/form/div/div[2]/button[2]"))).click()

print(arvore1)
for itens in arvore1:
    print(itens.text)
input("Digite enter para sair")

driver.quit()
