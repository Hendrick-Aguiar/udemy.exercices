#https://docs.python.org/3/library/functions.html
#map function
    #muito utilizado com listas
    #applicar um função a um iterable, por item. (list, tuple, dic etc)
lista = [1,2,3,4]
def mult(x):
    return x*2

lista2 = map(mult, lista)
print(list(lista2))