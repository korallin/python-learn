#Tuplas

#Listas

#Dicionarios

#Aula de Tupla

#lanche = () [] {} tupla, lista, dicionario
from builtins import enumerate

lanche = ('Hamburger','Suco','Pizza','Pudim')
print(lanche)

print(lanche[1])

print(lanche[-1])

print(lanche[1:3])

print(lanche[2:])

print(lanche[:2])

print(lanche[-3])

print(lanche)

#tuplas são imutaveis

#lanche[1]='Refigerante'
#print(lanche[1]) - Tupla não aceita receber diremente pelo elemento

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra carabma!')

for cont in range(0,len(lanche))
    print(lanche[cont])
print('Comi pra carabma!')

for comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição{pos}')
print('Comi pra caramba.')

print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c=a+b
print(c)

print(c.count(5))


print(c.index(2))

print(c.index(2:5))