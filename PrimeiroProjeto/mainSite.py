from selenium import webdriver
from enderecoWeb import EndWeb

browserMozila = webdriver.Firefox()
facebook = EndWeb()

browserMozila.get(facebook.getUrl())
browserMozila.find_element_by_name('email').send_keys(facebook.getUsuario())
browserMozila.find_element_by_name('pass').send_keys(facebook.getSenha())

button = browserMozila.find_element_by_name('login')
button.click()
