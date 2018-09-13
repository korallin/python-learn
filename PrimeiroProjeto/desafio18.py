#Faça um progrma que leia um âgulo qualquer e
# mostre na tela o valor do seno, cosseno e tangete
# desse ângulo.

from math import cos, sin, tan, radians

angulo = float(input('Informe o ângulo para calcular o seno e cosseno: '))
print('O seno deste ângulo radial é: {:.2f}.'.format(sin(radians(angulo))))
print('O cosseno deste ângulo radial é: {:.2f}.'.format(cos(radians(angulo))))
print('O tangente deste ângulo radial é: {:.2f}.'.format(tan(radians(angulo))))
