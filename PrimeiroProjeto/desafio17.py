# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimeito da hipotenusa.

print('Programa que calcula a hipotenusa')

catetoOposto = float(input('Favor informar o cateto oposto: '))
catetoAdjacente = float(input('Favor informar o cateto adjacente: '))

from math import sqrt, trunc, hypot

#a² + b² = c²
hipotenusa = sqrt(catetoOposto**2 + catetoAdjacente**2)
print(trunc(hipotenusa))
hipotenusa = (catetoOposto**2 + catetoAdjacente**2)**(1/2)
print(trunc(hipotenusa))
hipotenusa=hypot(catetoOposto,catetoAdjacente)
print(hipotenusa)

print('O comprimento da hipotenusa é: {}.'.format(
      sqrt(catetoOposto**2 + catetoAdjacente**2))
     )

