from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
#rom selenium.webdriver.common.WebElement import WebElement


browser = webdriver.Firefox()

#browser.get('https://vivocorp-parceiro.vivo.com.br/LoginAppV2/login.jsp')
browser.get('https://vivocorp-parceiro.vivo.com.br/vivocorp')
browser.find_element_by_name('username').send_keys('80053926')
time.sleep(5)
browser.find_element_by_name('password').send_keys('Stcbr@26')
browser.find_element_by_class_name('button').submit()
browser.submit()