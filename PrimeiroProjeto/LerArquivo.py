class LerArquivo():
	"""Classe que irá ler o arquivo com o usuário de senha do acesso do site"""
	def __init__(self):		
		self.arquivo = open('/home/home/Transferências/iniText.txt')
		self.site = list()

	def CarregarDados(self):		
		for line in self.arquivo:			
			self.site.append(line[(line.find('USUARIO')+8):(line.find('¨'))]) 
			self.site.append(line[(line.find('SENHA')+6):len(line)-1])	

	def PegarUsuarioSenha(self):
		self.CarregarDados()
		return self.site		