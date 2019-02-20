from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

browser = webdriver.Firefox()

browser.get('http://www.tjmg.jus.br/portal-tjmg/')

element = browser.find_element_by_name('txtProcesso')
codigoProcesso = '84881073120058130024'
element.send_keys(codigoProcesso)

chave = (codigoProcesso[11:13] + codigoProcesso[:6])

browser.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[1]/div[2]/section[1]/div/div[1]/div/div[1]/form/div[6]/button').click()

time.sleep(8)

vara = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[1]/b').text
status = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/b').text 

requerente = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr[1]/td[2]').text
requerido = browser.find_element_by_xpath('/html/body/table[4]/tbody/tr[2]/td[2]').text

time.sleep(2)

browser.get('https://www4.tjmg.jus.br/juridico/sf/proc_movimentacoes.jsp?comrCodigo=24&numero=1&listaProcessos='+ chave)

table_id = browser.find_element_by_class_name('tabela_formulario')
#rows = table_id.find_element_by_tag_name('tr') # get all of the rows in the table
#print(row.find_element_by_name('td')[1])
for tr in table_id.find_elements_by_tag_name('tr'):
    for td in tr.find_elements_by_tag_name('td'): 
#for row in rows:
        # Get the columns (all the column 2)        
        #col = row.find_element_by_name('td')#[1] #note: index start from 0, 1 is col 2
        print(td.text) #prints text from the element

print('Grid 2')

table_id = browser.find_element_by_xpath('/html/body/table[2]')

tabela = []

for tr in table_id.find_elements_by_tag_name('tr'):
    tabela.append('\n')
    for td in tr.find_elements_by_tag_name('td'): 
        #print(td.text) #prints text from the element        
        tabela.append(td.text)

name = ('../' + 'SaidaTexto.txt')

arquivo = open(name,'w')
arquivo.writelines(vara + '\n')
arquivo.write(status + '\n')
arquivo.write(requerente + '\n')
arquivo.write(requerido + '\n')

for lista in tabela:
    arquivo.write(lista)

arquivo.close
	