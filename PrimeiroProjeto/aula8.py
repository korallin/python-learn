from math import sqrt, floor, trunc
import random

num = int(input('Digite um número: '))
#num = random.randint(1,10)
raiz = sqrt(num)
#raiz = sqrt(random.randint(1,10))

print(trunc(raiz))

#print('A raiz do número aleatório é igual a {:.2f}'.format(num, floor(raiz)))
print('A raiz do número aleatório é igual a {:.2f}'.format(floor(raiz)))


