from classeFireFox import ClasseFirefox
from netFlix import NetFlix	

browser = ClasseFirefox()

netFlix = NetFlix()

browser.Acessar(netFlix.constUrl())

for elemento in netFlix.elementosEditText :
	browser.PreencherElemento(elemento['field'],elemento['conteudo'])

browser.SubMitElemento()