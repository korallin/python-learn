frase='Curso em Video Python'

print(frase[9])

print(frase[9:13])

print(frase[9:21])

print(frase[9:21:2])

print(frase[::2])

#Não sabe o início da posição da String
print(frase[:5])

#Não sabe o ultima posição da String
print(frase[15:])

#De um início específico até o final da String, pulando de 3 em 3 caracteres
print(frase[9::3])

#Comprimento da frase
print(len(frase))

#Quantidade de caracteres
print(frase.count('o'))

#Contar a quantidade de carcter de entre posicoes
print(frase.count('o',0,13))

#Encontrar o início da procura
print(frase.find('deo'))

#Caso não exista a String o Python retorna -1
print(frase.find('Android'))

#Operador para análise de texto
print('Curso' in frase)

print(frase)

#Metodo Replace
print(frase.replace('Python','Android'))

print(frase)

#Deixar Maisculo
print(frase.upper())

print(frase)

#Deixar Minusculo
print(frase.lower())

#Captlize, Deixar apenas o primeiro caractere maisculo
print(frase.capitalize())

#Deixar todas as primeiras letras em maiusculas
print(frase.title())

#Remover espaços desnecessários
print(frase.strip())

#Remover somente do lado direito
print(frase.rstrip())
print(frase.lstrip())

#Dividir String o conteudo de palavras em uma lista e cada palavra uma posição da lista
print(frase.split())

#Juntar
print('-'.join(frase))

print('''Eu quero que o texto
         seja exibidos em posições diferentes
         este  é um texte.''')

#Exibir na lista criada, uma posição específica
dividido=frase.split()
print(dividido[2][3])
