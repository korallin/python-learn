while true:
    print('Antes do Break')
    break
    print('Depois do Break')
print('FIM')

n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')