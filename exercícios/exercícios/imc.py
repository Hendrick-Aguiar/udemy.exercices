#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:



altura = float(input('qual a sua altura em metro?'))

genero = int(input('Qual seu genero?: 0 para Mulher e  1 para Homem: '))

if genero <= 0:
    print(f'seu mmc é : ',(62.1*altura) - 44.7 )


if genero > 0 :
    print(' seu mmc é: ', (72.7*altura) - 58)



#homens = (72.7*altura) - 58 
#mulheres = (62.1*) - 44.7