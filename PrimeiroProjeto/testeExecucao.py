path = '/home/work/Downloads/comprovante.jpg'

carac = '\/'

for i in range(len(path)-1,0,-1):
	if carac.find(path[i]) > -1:
		print(path[i])
		print(path[i+1:])
		print(path[:i+1])
		print(path[:i+1] + (path[i+1:]))
		break