# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Informe uma frase para o programa computar: ').strip().upper())

print('Total de letras A: {}'.format(frase.count('A')))

print('A primeira posição da letra A: {}'.format(frase.find('A')+1))

print('Ultima letra A: {}'.format(frase.rfind('A')+1))
