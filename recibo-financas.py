from selenium import webdriver
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from selenium.webdriver.firefox.options import Options

data_a_usar="2023-01-01"

receipt_start_date = datetime.strptime(data_a_usar, "%Y-%m-%d")
receipt_end_date   = receipt_start_date + relativedelta(months=1) - timedelta(days=1)
receipt_date = receipt_start_date - relativedelta(months=1) + timedelta(days=4)

print("Inicio:  " + datetime.strftime(receipt_start_date, "%Y-%m-%d"))
print("Fim:     " + datetime.strftime(receipt_end_date, "%Y-%m-%d"))
print("Emissao: " + datetime.strftime(receipt_date, "%Y-%m-%d"))

time.sleep(5)

#exit()
download_dir="C:\\Users\\<user>\\Documents\\"
options=Options()
options.set_preference("browser.download.dir", download_dir)
options.set_preference("browser.preferences.instantApply", True)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.set_preference("browser.helperApps.alwaysAsk.force", False)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.folderList", 2)
options.set_preference("pdfjs.disabled", True);

driver = webdriver.Firefox(options=options)

driver.get("https://imoveis.portaldasfinancas.gov.pt/arrendamento/")


# Escolher NIF
time.sleep(2)
element = driver.find_element(by='xpath', value='//*[text()="NIF"]')
driver.execute_script("arguments[0].click();", element)


# Login 
element = driver.find_element(by='id', value="username")
element.send_keys("<NIF>")
element = driver.find_element(by='id', value="password-nif")
element.send_keys("<Password>")
element = driver.find_element(by='id', value="sbmtLogin")
element.click()

# Emitir recibo
time.sleep(2)
element = driver.find_element(by='link text', value="EMITIR RECIBO RENDA")
element.click()

time.sleep(2)
#element = driver.find_element(by='xpath', value='//*[text()="Emitir Recibo"]')
element = driver.find_element(by='xpath', value='//*[text()=" <Descricao do Imovel no site das Finanças>"]')
driver.execute_script("arguments[0].click();", element)

time.sleep(2)
element = driver.find_element(by='xpath', value='//*[@ng-model="recibo.dataInicio"]')
element.send_keys(datetime.strftime(receipt_start_date, "%Y-%m-%d"))
element = driver.find_element(by='xpath', value='//*[@ng-model="recibo.dataFim"]')
element.send_keys(datetime.strftime(receipt_end_date, "%Y-%m-%d"))
element = driver.find_element(by='xpath', value='//*[@ng-model="recibo.dataRecebimento"]')
element.send_keys(datetime.strftime(receipt_date, "%Y-%m-%d"))

element = driver.find_element(by='xpath', value='//*[@ng-value="catalogos.tiposImportancia.renda"]')
element.click()

element = driver.find_element(by='xpath', value='//*[text()="Emitir"]')
driver.execute_script("arguments[0].click();", element)


time.sleep(3)
element = driver.find_element(by='xpath', value='//*[text()="Imprimir"]')
driver.execute_script("arguments[0].click();", element)



print(element)
time.sleep(10)

#close browser
driver.quit()
