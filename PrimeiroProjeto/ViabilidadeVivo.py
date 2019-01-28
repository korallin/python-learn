from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
#rom selenium.webdriver.common.WebElement import WebElement


browser = webdriver.Firefox()

browser.get('https://vivocorp-parceiro.vivo.com.br/LoginAppV2/login.jsp')
browser.find_element_by_name('username').send_keys('800539268')
time.sleep(3)
browser.find_element_by_name('password').send_keys('Stcbr@26')
browser.find_element_by_class_name('button').submit()
browser.submit()