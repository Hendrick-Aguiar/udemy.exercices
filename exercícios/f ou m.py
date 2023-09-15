#Faça um Programa que verifique se uma letra digitada é "F" ou 
# "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Digite F para Feminino ou M para Masculino'))




if sexo == 'f' or sexo == 'F':
    print('feminino')
    
elif sexo  == 'm' or sexo == 'M':
    print('masculino')
else:
    print('sexo invalido')
