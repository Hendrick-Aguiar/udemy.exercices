print('olá mundo')#print
print(5*3)#álgebra
print(5**3)
a = 3 #variáveis
b = 6
soma = a + b
print(soma)
soma = a + b # junção de variáveis com texto
quadrado = soma ** 2
print(' a soma é', soma, 'o quadrado da soma é', quadrado), 

c = 3 #condicionais if
d = 5
cálculo = c + d
if cálculo == 8:
    print('a soma é 8', cálculo)
else:
     print('não é 8')
  
frase = 'python em 10 min'#loop
for n in range(5): #loop

    print(n)
    print(frase)
         
nome = input('qual o seu nome?') #inputs
print(nome)
idade = int(input('qual a sua idade'))# para somar numero inserido em variáveis é necessário transformá-la em int()
print(idade *2)

def somar_dois_numeros(): #funções
   numero1 = 10
   numero2 = 5
   resultado = numero1 + numero2
   print(resultado)
   
   
somar_dois_numeros() 

#parâmentros---->argumentos


def boas_vindas(nome, quantidade):
    print(f'olá {nome}.')
    print(f'temos {quantidade} laptops em estoque')

boas_vindas('Marcos', 5)
boas_vindas('Fulano', 5)
boas_vindas('Enzo', 5)
'''
def boas_vindas_marcos(): # Forma comum e acima simplificada
    print('olá marcos')
    print('temos 5 laptops em estoque')
    
    
def boas_vindas_fulano():
    print('olá Fulano')
    print('temos 5 laptops em estoque')


def boas_vindas_Enzo():
    print('olá Enzo')
    print('temos 5 laptops em estoque')


boas_vindas_marcos()
boas_vindas_fulano()
boas_vindas_Enzo()''

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
