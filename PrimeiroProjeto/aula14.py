#Enquanto

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par +=1
    else:
        impar +=1
print('Você digitou {} números pares e {} números ímpares'.format(par,impar))

