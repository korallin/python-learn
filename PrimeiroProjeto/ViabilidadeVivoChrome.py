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
browser.find_element_by_name('username').send_keys('80053926')

time.sleep(3)

browser.find_element_by_name('password').send_keys('Stcbr@26')
browser.find_element_by_class_name('button').click()
'''
time.sleep(3)

browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=Login&SWEPL=1&_sn=kTuq3U-.'+
            'yAskPIqVpdOZySgYP5A6dpFZNfShfscSl5lE42eExFp.qh0BQCM6Y5IBTVHpv9Ve.YVK7TlDYIF8rSlv45o.L3-BAgHTLN'+
            '9DA1UWMaXfth22IJZurNPI4pt-MznBdEgdb4-bP1OzpLjdrkpB4EwtggLUo-zHRLtes5n4Ha74D1ztFDRHt7ahVu4Ywr0z'+
            'G96iYSk_&SRN=K1gekGBBjDd2PK6mmPP8IhvLCopcVSAuJZ10utLGhJ0b&SWETS=')
'''
browser.submit()

browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[1]/ul/li[3]').click()

browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[2]/ul/li[3]').click()

browser.find_element_by_id('s_1_1_16_0_Ctrl').click()

browser.find_element_by_xpath('//*[@id="1_s_1_l_VIVO_Documento"]').click()

browser.find_element_by_xpath('//*[@id="1_VIVO_Documento"]').send_keys('08661552605') 

browser.find_element_by_id('s_1_1_8_0_Ctrl').click()