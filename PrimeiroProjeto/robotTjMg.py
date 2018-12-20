from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()

browser.get('http://www.tjmg.jus.br/portal-tjmg/')

element = Select(browser.find_element_by_name('tipoPesquisa'))
element.select_by_index(2)



	