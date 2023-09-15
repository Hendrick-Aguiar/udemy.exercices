
#dicionários
    #utiliza index no formato de keys e values
    #aceita strings, intergers, float, boolean...

aluno = {'nome': 'ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}
# consegue se imprimir tanto keys e values com o comando do for loop
for keys, values in aluno.items():
    print(keys, values)