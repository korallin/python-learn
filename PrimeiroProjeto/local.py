from PIL import Image 

import pytesseract 

endereco = '/home/work/Downloads/comprovante.jpg'
	




print( pytesseract.image_to_string( Image.open(endereco), lang='por' ) ) # Extraindo o texto da imagem

