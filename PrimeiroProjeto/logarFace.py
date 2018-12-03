from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.facebook.com/login')
browser.find_element_by_name('email').send_keys('aliem82@msn.com')

browser.find_element_by_name('pass').send_keys('mikel2151*.')

elemento = browser.find_element_by_name('login')
elemento.click()

