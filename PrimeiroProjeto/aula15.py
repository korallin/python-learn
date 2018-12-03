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
print('A soma vale {s}'.format(s))
print(f'O {s:-^0} tem {s} anos e  ganha R${S:.2F}')