from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

#80053926 - Stcbr@26; 80003010 - P@ssword12

browser.get('http://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Contas+Detail+-+Contacts+View&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1')
browser.find_element_by_name('username').send_keys('80003010')
time.sleep(3)
browser.find_element_by_name('password').send_keys('P@ssword12')
browser.find_element_by_class_name('button').submit()
#browser.submit()
#browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Hierarquia+de+Contas&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1#s_sctrl_tabView_noop')
#Aba Contas
#Tempo de 70 para 130
try:
    WebDriverWait(browser,130).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]')))
#except WebDriverException:
finally:
    pass

#Sub Aba Contas
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3]').click()
time.sleep(3)
#Sub Aba Hierarquia
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]').click()

WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.ID,'s_1_1_16_0_Ctrl')))

#Aba Botao Pesquisar
browser.find_element_by_id('s_1_1_16_0_Ctrl').click()
#Aba Fiedl CNPJ
browser.find_element_by_xpath('//*[@id="1_s_1_l_VIVO_Documento"]').click()
#Aba INSERIR CNPJ
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
#EDIT SOBRENOME 
sobrenome = browser.find_element_by_id('1_s_1_l_Last_Name').get_attribute('title')
#EDIT CELULAR
celular = browser.find_element_by_id('1_s_1_l_Cellular_Phone__').get_attribute('title')
#EDIT FIXO
telefoneFixo = browser.find_element_by_id('1_s_1_l_Work_Phone__').get_attribute('title')
#EDIT EMAIL
email = browser.find_element_by_id('1_s_1_l_Email_Address').get_attribute('title')
#EDIT ENDERECO
endereco = browser.find_element_by_name('s_3_1_160_0').get_attribute('value')
#EDIT NUMERO
enderecoNumero = browser.find_element_by_name('s_3_1_58_0').get_attribute('value')
#EDIT COMPLEMENTO
#complemento = browser.find_element_by_id('').get_attribute('value')
#EDIT CEP
cep = browser.find_element_by_name('s_3_1_195_0').get_attribute('value')

name = ('C:/Chromedriver/' + 'SaidaTexto.txt')

arquivo = open(name,'w')
arquivo.writelines(primeiroNome + '\n')
arquivo.write(sobrenome + '\n')
arquivo.write(celular + '\n')
arquivo.write(telefoneFixo + '\n')
arquivo.write(email + '\n')
arquivo.write(endereco + '\n')
arquivo.write(enderecoNumero + '\n')
arquivo.write(cep + '\n')
arquivo.close