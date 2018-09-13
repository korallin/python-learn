#Escreva um programa que faça o compuutador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar descobir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdu.

print('Eu sou um computador pensante! Pensei em um número de 0 à 5, tente descobri-lo.')

from random import randint
numeroPensado = randint(0,5)

numeroUsuario = int(input('Faça sua tentativa, informe um número: '))

if numeroPensado == numeroUsuario:
    print('Você acertou o número pensado pelo computador. ')
else:
    print('Infelizmente você não acertou. Mais sorte na próxima vez.')

print('Você acertou!' if numeroUsuario==numeroPensado else 'Deu ruim!')

