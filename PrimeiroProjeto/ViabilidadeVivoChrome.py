from selenium import webdriver
import time

#abrir configuracao arquivo
config = open('C:/Chromedriver/CONFIG.txt','r')
line = config.readline()
ini = line[13:]
config.close()

#'C:/Chromedriver/chromedriver.exe'
driver = (ini) 
browser = webdriver.Chrome(driver)

browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp')
browser.find_element_by_name('username').send_keys('80053926')

time.sleep(3)

browser.find_element_by_name('password').send_keys('Stcbr@26')
browser.find_element_by_class_name('button').submit()
browser.submit()