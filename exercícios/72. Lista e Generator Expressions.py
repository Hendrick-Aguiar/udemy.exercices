#generator expressions 
    #uma forma mais rápida para listas, dicionários e etc
    #menos memória alocada
    #valores em bytes

numeros = (x * 10 for x in range(100))


print(type(numeros))
print(list(numeros))
print(getsuz(numeros))
