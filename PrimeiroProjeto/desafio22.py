#Crie um programa que leia o nome completo de uma pessoa e mostra:
# * O nome com todas as letras maiúsculas.
# * O nome com todas minúsculas
# * Quantas letras ao todo(sem considerar espaços)

nomeCompleto = input('Favor informar o seu nome completo!')

print(nomeCompleto.upper())

print(nomeCompleto.lower())

print(len(nomeCompleto.strip()))

print(len(nomeCompleto) - nomeCompleto.count(' '))

print(nomeCompleto.strip().find(' '))

print(len(nomeCompleto.strip().split()[0]))


