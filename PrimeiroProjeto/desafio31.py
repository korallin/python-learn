#Desenvolver um programa que pergunte a distância de uma viagem dem KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = int(input('Favor informar a distância estimada da viagem: '))

if distancia<=200:
    valorPassagem=distancia*.50
    print('O valor da passagem é {:.2f}'.format(valorPassagem))
else:
    valorPassagem=distancia*.45
    print('O valor da passagem é {:.2f}'.format(valorPassagem))