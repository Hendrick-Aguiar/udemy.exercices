#funções(functions)
    #dry don't repeat yourself
    #vários argumentos (xargs) ou * identificando o Parâmetro
#criar uma função que armazena números e strings (dados)
# motivos: adicionar vários argumentos e ao mesmo tempo
# identificando os elementos, para que assim 
# COM DOIS ASTERISCOS(**) POSSO PASSAR ARGUMENTOS E PARAMETROS EM UM FUNÇÃO





def agencia(**carro):
    return carro

print(agencia(marca='gol', cor='branca', motor=1.0, placa=123456))
print(agencia(marca='gol', cor='branca', motor=1.0, placa=123456))
print(agencia(marca='celta', cor='branca', motor=1.0, placa=123456))
print(agencia(marca='corsa', cor='branca', motor=1.0, placa=123456))
