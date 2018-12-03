from selenium import webdriver

class ClasseFirefox():	
	def __init__(Self,browserMozila=None):
		Self.browserMozila = webdriver.Firefox()

	def Acessar(Self,url):
		Self.browserMozila.get(url)		

	def Logar(Self, site, usuario, senha):
		Self.browserMozila.find_element_by_name(site.constElementUsuario()).send_keys(usuario)
		Self.browserMozila.find_element_by_name(site.constElementSenha()).send_keys(senha)

	def CapturarElemento(Self, nomeElemento):		
		return Self.browserMozila.find_element_by_name(nomeElemento)

	def PreencherElemento(Self, elemento, elementoValor):
		editText = Self.CapturarElemento(elemento)
		editText.send_keys(elementoValor)

	def ClickElemento(Self, elemento):
		button = Self.CapturarElemento(elemento)
		button.click()

	def SubMitElemento(Self):
		#button = Self.browserMozila.find_element_by_class_name('').submit
		button = Self.browserMozila.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').submit()
		





