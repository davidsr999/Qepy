import sys



command = sys.argv[1:]
lista = []
lista2 = []
N = len(command)
for n in range(N):
    if command[n][:2]=='--':
        lista.append(command[n][2:])
        lista2.append(command[n+1])
print(lista)
print(lista2)

