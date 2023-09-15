'''import random
numeros = []
while len(numeros)< 10:
    numero=random.randint(1,100)
    if numero  not in numeros:
        numeros.append(numero)
        print(sorted(numeros))'''

lista = [5, 7, 3, 6]
pos = 2
for i in range(len(lista)-1, pos-1, -1):
    lista[i] = lista[i-1] 
lista pos-1]=8
print(lista)