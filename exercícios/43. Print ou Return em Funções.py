#functions
    # do not repeat yourself (dry)
    #realizam uma tarefa
    #calcula e retorna um valor

from http import client


def cliente(nome):
    print(f' Olá {nome}') 
    
def client2(nome):
    return f' olá {nome}'

cliente('maria')
cliente('josé')

x = client2('maria')
y = client2('Jose')

print(x)
print(y)

