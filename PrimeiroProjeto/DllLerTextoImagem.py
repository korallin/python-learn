from PIL import Image 
import pytesseract 

class DllLerImagem:
	def __init__(self,path):
		self.enderecoImagem = path	
		self.arquivoImagem = ''
		self.RetornarTextoImagem()	

	def FormatarEndereco(Self,endereco):
		self.enderecoImagem = string(endereco).strip()

	def AbrirImagem(self):
		Image.open(self.enderecoImagem)		

	def ConverterImagemParaString(self):
		return pytesseract.image_to_string(Image, lang='por')		

	def RetornarTextoImagem(self):
		self.FormatarEndereco(self.enderecoImagem)
		AbrirImagem()
		self.arquivoImagem = self.ConverterImagemParaString()
		print( self.arquivoImagem )		


dll = DllLerImagem('/home/work/Downloads/Conciliao61.jpg')

#print( pytesseract.image_to_string( Image.open(endereco), lang='por' ) ) # Extraindo o texto da imagem