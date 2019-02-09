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
    print('antes do WebDriverWait')
    #WebDriverWait(browser,40).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3]')))
    browser.implicitly_wait(70)
    #wait = WebDriverWait(browser, 10)
    #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hplogo"]')))  #element_to_be_selected
    print('depios do WebDriverWait')
except WebDriverException:
    pass

print('pós try')
#Sub Aba Hierarquia
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]').click()
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
#RESULTADO
#EDIT PRIMEIRO NOME
primeiroNome = browser.find_element_by_id('1_First_Name').get_attribute('value')
#EDIT SOBRENOME
sobrenome = browser.find_element_by_id('1_Last_Name').get_attribute('value')
#EDIT CELULAR
celular = browser.find_element_by_id('1_Cellular_Phone__').get_attribute('value')
#EDIT FIXO
telefoneFixo = browser.find_element_by_id('1_s_1_l_Work_Phone__').get_attribute('value')
#EDIT EMAIL
email = browser.find_element_by_id('1_s_1_l_Email_Address').get_attribute('value')
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
arquivo.write(primeiroNome)
arquivo.write(sobrenome)
arquivo.write(celular)
arquivo.write(telefoneFixo)
arquivo.write(email)
arquivo.write(endereco)
arquivo.write(enderecoNumero)
arquivo.write(cep)
arquivo.close