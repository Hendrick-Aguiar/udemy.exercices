#armazenar mais de uma informação em variáveis
# manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5,6,7]
# o * asterísco associa todas as variáveis               0         1         2         3  
item1, item2, *outros, item8, = produtos


print(item1)
print(item2)
print(outros)