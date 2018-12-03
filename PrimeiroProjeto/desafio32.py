#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Informe um ano: '))

if ano % 4 == 0:
    if ano  % 100 != 0:
        print('Ano é bissexto!')
    else:
        print('Ano não é bissexto!')
else:
    if ano % 400 == 0:
        print('Ano é bissexto!')
    else:
        print('Ano não é bissexto!')