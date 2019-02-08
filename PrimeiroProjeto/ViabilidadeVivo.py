from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#from selenium.webdriver.common.by import By
#rom selenium.webdriver.common.WebElement import WebElement


browser = webdriver.Firefox()

#browser.get('https://vivocorp-parceiro.vivo.com.br/LoginAppV2/login.jsp')
browser.get('http://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Contas+Detail+-+Contacts+View&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1')
browser.find_element_by_name('username').send_keys('80053926')
time.sleep(3)
browser.find_element_by_name('password').send_keys('Stcbr@26')
browser.find_element_by_class_name('button').submit()
browser.submit()

time.sleep(15)
#browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp_oui/start.swe?SWECmd=GotoView&SWEView=VIVO+Hierarquia+de+Contas&SWERF=1&SWEHo=vivocorp-parceiro.vivo.com.br&SWEBU=1#s_sctrl_tabView_noop')

element = Select(browser.find_element_by_id('s_sctrl')) 
element.select_by_index(3)