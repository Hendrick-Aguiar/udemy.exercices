
#usar | union lista 1 e lista 2
# usar s
#lista1 trabalham durante o dia
#lista2 trabalham durante a noite
#lista3 trabalha não tem carro

funcionarios = {'ana', 'marcos', 'alice', 'pedro', 'sophia', 'bruno', 'melissa'}
turno_dia = {'ana', 'marcos', 'alice', 'melissa'}
turno_noite = {'pedro', 'sophia', 'bruno'}
tem_carro = {'marcos','alice', 'bruno', 'melissa'}

nomes = set(funcionarios)
lista1 = turno_noite.intersection(tem_carro) #mostra igualdade entre as duas listas
lista2 = turno_dia.intersection(tem_carro)
lista3 = funcionarios.difference(tem_carro) #mostra oque não está repetido entre as duas listas
print(f'{lista1}, tem carro e trabalha a noite')
print(f'{lista2} tem carro e trabalham a noite')
print(f'{lista3} Não tem carro')

