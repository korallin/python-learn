#Escreva um programa que pergunte o salário de um funcionário e calcule seu valor de aumento. Para salários superiores
# a 1250,00 calcule um aumento de 10% para inferiores ou iguais  o aumento é de 15%.

salario = float(input('Informe o seu salário: '))

if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print('O aumento de salário final com o aumento será: {:.2f}.'.format(aumento))
