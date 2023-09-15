#tuples
    #armazenar mais de uma informção em variaveis
    #mater a seuqncia dos dados em uma variavel
    #não podem ser alteradas (imutable)
cores_lista = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuples = ('amarelo', 'verde', 'azul', 'vermelho')

#vantagens do tuple é o menor consumo de memória
print(type(cores_lista))
print(type(cores_tuples))

duas_listas = cores_tuples*2
#(cores_tuples).append('roxo') no tuple não é possivel modificar itens
(cores_lista).append('roxo') #lista é possivel alterar itens
print(cores_lista)
