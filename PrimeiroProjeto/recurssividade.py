'''
Fatorial
0! = 1
3! = 3 * 2 * 1 = 6
'''
#Implementação recurssiva
def fat(n):
	if n == 0:
		return 1
	return n * fat(n - 1)

print(fat(5))