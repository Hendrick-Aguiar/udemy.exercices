#criar uma classe
from mailbox import NotEmptyError


class Funcionarios:
#argumentos
    def __init__(self, nome, sobrenome, data_nascimento): #
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
       
    
        
#criar objetos
usuario1 = Funcionarios('elena', 'cabral', '12/08/1989')
usuario2 = Funcionarios('carol', 'braga', '14/05/1879')

print(usuario1.nome)
print(usuario2.sobrenome)
#criar os parametros
'''
usuario1.sobrenome = 'cabral'
usuario1.data_nascimento = '16/12/1925'

usuario2.nome = 'vicentina'
usuario2.sobrenome = 'sacani'
usuario2.data_nascimento = '18/07/2222'
#print

'''