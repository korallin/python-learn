#23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
#um dos dígitos separados.

string = input('Digite um número de 0 a 9999')
#string = string.split()

qtd=len(string)
print('{0:>7}: {1}'.format('Unidade',string[(qtd-1)]))

if (qtd>1):
    print('{0:>7}: {1}'.format('Dezena',string[(qtd-2)]))
    if (qtd>2):
        print('{0:>7}: {1}'.format('Centena',string[(qtd-3)]))
        if (qtd>3):
            print('{0:>7}: {1}'.format('Milhar',string[(qtd-4)]))


