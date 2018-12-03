class LerCampos():
	"""Classe que irá ler o arquivo com o usuário de senha do acesso do site"""
	def __init__(self):		
		self.arquivo = open('/home/home/Transferências/MapFace.txt')
		self.campos = list()
		self.submit = None

	def CarregarDados(self):		
		for line in self.arquivo:			
			if line[4] == 'D':
				if line[75:(75+10)].strip() == 'EDIT':					
					self.campos.append(line[30:(30+45)].strip())
					print(self.campos,'campo')
				elif line[75:(75+10)].strip() == 'SUBMIT':					
					self.submit(line[30:(30+45)].strip())
					print(self.submit,'submit')

	def PegarCampos(self):
		self.CarregarDados()
		return self.campos		


ler = LerCampos()
ler.PegarCampos()		