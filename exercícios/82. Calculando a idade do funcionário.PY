from datetime import datetime
#criar as clases
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento): #criada para monta os construtores
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    def nome_completo(self):# criada para mostrar o nome completo
        return (self.nome + ' ' + self.sobrenome)
#função criada para mostrar o ano de nascimento importando o datetime
# o self deve ser sempre citado     
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
#criar objetos        
usuario1 = Funcionarios('elena', 'cabral', 2000)
usuario2 = Funcionarios('carol', 'braga', 1989)

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.nome_completo(usuario2))
    