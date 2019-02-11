from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

#browser.get('https://vivocorp-parceiro.vivo.com.br/LoginAppV2/login.jsp')
browser.get('http://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Contas+Detail+-+Contacts+View&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1')
browser.find_element_by_name('username').send_keys('80053926')
time.sleep(3)
browser.find_element_by_name('password').send_keys('Stcbr@26')
print('pós senha')
browser.find_element_by_class_name('button').submit()
#browser.submit()
print('antes do try')
#browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Hierarquia+de+Contas&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1#s_sctrl_tabView_noop')
#Aba Contas
try:
    print('antes do WebDriverWait 70')
    WebDriverWait(browser,60).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]')))
    print('depios do WebDriverWait')
#except WebDriverException:
finally:
    pass

print('pós try')
#Sub Aba Contas
print('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3] 1 ')
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3]').click()
time.sleep(3)
#Sub Aba Hierarquia
print('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]') 
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]').click()

WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.ID,'s_1_1_16_0_Ctrl')))

#Aba Botao Pesquisar
print('s_1_1_16_0_Ctrl')
browser.find_element_by_id('s_1_1_16_0_Ctrl').click()
#Aba Fiedl CNPJ
print('//*[@id="1_s_1_l_VIVO_Documento"]')
browser.find_element_by_xpath('//*[@id="1_s_1_l_VIVO_Documento"]').click()
#Aba INSERIR CNPJ
print('//*[@id="1_VIVO_Documento"]')
browser.find_element_by_xpath('//*[@id="1_VIVO_Documento"]').send_keys('59120493000146') 
#Aba BOTAO IR
browser.find_element_by_id('s_1_1_8_0_Ctrl').click()
time.sleep(3)
#LINK CADASTRO CLIENTE
browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[6]/div/div[1]/div/div[1]/div/div/form/span/div/div[2]/div/div/div[3]/div[3]/div/table/tbody/tr[2]/td[10]/a').click()

WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.ID,'1_s_1_l_First_Name')))

#RESULTADO
#EDIT PRIMEIRO NOME 
primeiroNome = browser.find_element_by_id('1_s_1_l_First_Name').get_attribute('title')
print(primeiroNome)
#EDIT SOBRENOME 
sobrenome = browser.find_element_by_id('1_s_1_l_Last_Name').get_attribute('title')
print(sobrenome)
