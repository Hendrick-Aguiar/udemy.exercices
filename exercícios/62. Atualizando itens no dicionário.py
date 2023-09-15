#dicionários
    #Utiliza index no formato de keys e values
    #aceita string, integer, float, boolean

aluno = {'nome': 'ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

#aluno['nome'] = 'jose'
#aluno.update({'nome': 'jose', 'nota final': 'b', 'aprovação': True })
#aluno.update({'endereço': 'rua a'})
#print (aluno.get('endereço','não existe'))
del aluno['idade']
print(aluno)
