#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o onme deles e escrevendo o nome do escolhido.

alunos = []
    #['d','a','e','g']

for i in range(4):
    alunos.append(input('Inform o nome do {}º aluno(a): '.format(i+1)))

from random import random, randint

escolhido = randint(0,3)
print(escolhido)

print('O escolhido para apagar o quadro  é o(a) aluno(a) {}'.format(alunos[escolhido]))