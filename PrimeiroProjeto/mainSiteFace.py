from classeFireFox import ClasseFirefox
from facebook import Facebook	

facebook = Facebook()

browser = ClasseFirefox()
browser.Acessar(facebook.constUrl())


for elemento in facebook.constElementosEditText():	
	browser.PreencherElemento(elemento['field'],elemento['conteudo'])

#browser.ClickElemento('login')
browser.ClickElemento(facebook.constSubmit())
