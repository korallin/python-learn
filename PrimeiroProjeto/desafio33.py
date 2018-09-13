#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1=int(input('Informe o primeiro número: '))

num2=int(input('Informe o segundo número: '))

num3=int(input('Informe o terceiro número: '))

maior=num1
if num2>num1:
    maior=num2
if num3>maior:
    maior=num3

print('O maior número informado é {}'.format(maior))

menor=num1
if num2<num1:
    menor=num2
if num3<menor:
    menor=num3

print('O menor número informado é {}'.format(menor))