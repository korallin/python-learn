from LerArquivo import LerArquivo
from lerCampos import LerCampos

class Facebook:
	def __init__(self):
		self.url = 'https://www.facebook.com/login'
		self.usuario = 'aliem82@msn.com'
		self.senha = 'mikel2151*.'		
		self.constElementos = ['email','pass']		
		self.constSubmit = None
		self.elementos = self.CarregarArquivoCampos()
		self.config = self.CarregarConfig()        
		self.elementosEditText = self.ProcessarConfiguracao()

	def CarregarArquivoCampos(self):
		configC=LerCampos()        
		return configC
    
	def CarregarConfig(self):
		config=LerArquivo()        
		return config

	def ProcessarConfiguracao(self):	
		lista = self.config.PegarUsuarioSenha()			
		retorno = list()

		dic = dict()
		for i in range(0,len(lista)):						
			dic['field'] = str(self.constElementos[i])			
			dic['conteudo'] = str(lista[i])									
			retorno.append(dic.copy())					
		return retorno
			
	def constUrl(self):
		return self.url	

	def constElementUsuario(self):
		return self.elementUsuario

	def constElementSenha(self):
		return self.elementSenha		

	def constElementosEditTextManual(self):
		return self.elementosEditText		

	def constElementosEditText(self):
		return self.elementosEditText		

	#UsuarioTeste
	def constUsuario(self):
		return self.usuario

	def constSenha(self):
		return self.Senha		