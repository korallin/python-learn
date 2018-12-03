#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada kM acima do limite.

velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80.0:
    valorMulta = (velocidade-80) * 7
    print('A multa a ser paga será no valor de R$ {:.2f}'.format(valorMulta))
