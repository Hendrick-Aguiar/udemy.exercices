#set(listas)
    #similar a listas
    #evita itens duplicados
    #não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'f'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set3)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)