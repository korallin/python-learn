#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem formar ou não um triângulo

from random import randint

reta1 = int(input('Informe a primeira reta '))
reta2 = int(input('Informe a segunda reta '))
reta3 = int(input('Informe a terceira reta '))

if reta1 + reta2 > reta3:
    print('Forma um triângulo!')
