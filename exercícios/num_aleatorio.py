import random
num_entrada = int(input('Chute um número de 1 a 10: '))
aleatorio = random.randint(0,10)

if num_entrada < aleatorio:
    print('acima')
elif num_entrada > aleatorio:
    print('abaixo')
elif num_entrada > aleatorio:
    print('Digite um número abaixo de 10')
elif num_entrada == aleatorio:
    print('PARABÉNS ACERTOU!!!')
    


4