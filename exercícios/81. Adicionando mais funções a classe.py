


class Funcionarios:
#argumentos
    def __init__(self, nome, sobrenome, data_nascimento): #
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    def nome(self):
        return self.nome + ' ' + self.sobrenome   
    
    
        
#criar objetos
usuario1 = Funcionarios('elena', 'cabral', '12/08/1989')
usuario2 = Funcionarios('carol', 'braga', '14/05/1879')

print(usuario1.nome)
print(Funcionarios.nome(usuario1))
 