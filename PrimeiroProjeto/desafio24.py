#Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome SANTO

cidade = input('Informe o nome de uma cidade: ').strip().upper().split()

print('SANTO' in cidade[0])