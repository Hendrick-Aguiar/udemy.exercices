#funções
      #do not repeat yourself
      #parametro----> argumento
      #default = aquele que define o valor no parâmetro(nome)
      #non-default = Aquele que voce não define o valor do parâmentro(quantidade)
# default sempre depois! oque não muda de valor
#non-default(aquele que modifica os valores) Primeiro!


def boas_vindas(nome, quantidade=6 ):
    print(f'olá {nome}.')
    print(f'temos {quantidade} laptops em estoque')

boas_vindas(6)

