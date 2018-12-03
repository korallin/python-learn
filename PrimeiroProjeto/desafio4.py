print('Programa pega entrada e decifra o que é?')

entrada = input('Por favor, informe um caractere: ')
print('O caractere informado {0} é do tipo {1}'.format(entrada,type(entrada)))
print('Ele é do tipo numério: ',entrada.isnumeric())
print('Ele é do tipo alfabeto: ',entrada.isalpha())
print('Ele é do tipo alfa numerico: ',entrada.isalnum())
