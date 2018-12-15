class NetFlix:
	def __init__(self):
		self.url = 'https://www.netflix.com/br/login'
		self.usuario = 'rafael.dantas.monje@outlook.com'
		self.Senha = '17541754'		
		self.elementUsuario = 'userLoginId'
		self.elementSenha = 'password'
		self.elementosEditText = [{'field':self.elementUsuario, 'conteudo':self.usuario},
		                          {'field':self.elementSenha, 'conteudo':self.Senha}]			 

	def constUrl(self):
		return self.url	

	def constElementUsuario(self):
		return self.elementUsuario

	def constElementSenha(self):
		return self.elementSenha		

	def constElementosEditText(self):
		print (type(self.elementosEditText))
		return self.elementosEditText		

	#Us