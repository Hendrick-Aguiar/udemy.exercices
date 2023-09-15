#functions
    #dry
    #vários argumentos(x'args)
# PEGA UM RESULTADO E SOMA COM UM NUMERO
#criar uma função que soma vários números.
# O RESULTADO É 0 e a soma está sendo realizada dentro do for loop
# x=somas(2,3,4,7)soma=0+2=2 0 somado ao primeiro numero da lista/
# depois o próximo número é 3 que será somado: 2+3 que é = 5 sucessivamente... 
# até que o resultado final seja 16

def soma(*numeros):
    resultado = 0  
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7)

print(x)