tempo = int(input('Quanto antos tem o seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro usado')
print('--FIM--')

print('carro novo' if tempo<=3 else 'carro velho')

#PARTE 2
nome = str(input('Qual é o seu nome? '))
if nome == 'Michael':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

#PARTE 3
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns')
else:
    print('ESTUDE MAIS!')