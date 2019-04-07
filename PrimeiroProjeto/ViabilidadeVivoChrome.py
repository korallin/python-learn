from selenium import webdriver
import time

#abrir configuracao arquivo
config = open('C:/Chromedriver/CONFIG.txt','r')
line = config.readline()
ini = line[13:(line.find('exe')+3)]
line = config.readline()
user = line[5:(line.find('¨'))]
line = config.readline()
passw = line[5:(line.find('¨'))]
config.close()

print(user + ' - ' + passw)

#'C:/Chromedriver/chromedriver.exe'
driver = (ini) 
browser = webdriver.Chrome(driver)

browser.get('http://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Contas+Detail+-+Contacts+View&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1')
#browser.find_element_by_name('username').send_keys('80053926')
#browser.find_element_by_name('username').send_keys('80003010')
browser.find_element_by_name('username').send_keys(user)

time.sleep(3)

#browser.find_element_by_name('password').send_keys('Stcbr@26')
#browser.find_element_by_name('password').send_keys('P@ssword12')
browser.find_element_by_name('password').send_keys(passw)
browser.find_element_by_class_name('button').click()
'''
time.sleep(3)

browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=Login&SWEPL=1&_sn=kTuq3U-.'+
            'yAskPIqVpdOZySgYP5A6dpFZNfShfscSl5lE42eExFp.qh0BQCM6Y5IBTVHpv9Ve.YVK7TlDYIF8rSlv45o.L3-BAgHTLN'+
            '9DA1UWMaXfth22IJZurNPI4pt-MznBdEgdb4-bP1OzpLjdrkpB4EwtggLUo-zHRLtes5n4Ha74D1ztFDRHt7ahVu4Ywr0z'+
            'G96iYSk_&SRN=K1gekGBBjDd2PK6mmPP8IhvLCopcVSAuJZ10utLGhJ0b&SWETS=')
'''
browser.submit()

#browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Hierarquia+de+Contas&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1#s_sctrl_tabView_noop')
#Sub Aba Contas
print('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3] 1 ')
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3]').click()
time.sleep(3)
#Sub Aba Hierarquia
print('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]') 
browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]').click()
#Aba Botao Pesquisar
print('s_1_1_16_0_Ctrl')
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