#listas
    # ARMAZENAR mais de uma informação em variáveis
    # manter a sequência dos dados em uma variável
         #         0                  1
itens = [['item1', 'item2'], ['item3', 'item4']]
         #    0        1          2        3
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']
final = numeros + letras
numeros.extend(letras) #extend:pegar minha lista de numeros e extendo ela com as letras
print(numeros, itens[1][0])# 1º chamada se refere a lista externa, 
#2ª chamada se refere a lista interna, assim pode-se fazer duas chamadas lista/sublista
