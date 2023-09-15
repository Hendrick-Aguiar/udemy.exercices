# mostrar o ponto da carne

temperatura = int(input('insira a temperatura: '))

if temperatura < 48:
    print('NÃO ESTÁ PRONTA, AGUARDE!')

elif temperatura  in range(49, 55):
    print('mal passada')

elif temperatura in range(49, 55):
    print('ao ponto')

elif temperatura in range(56, 60):
    print('bem passada')

elif temperatura in range(61, 70):
    print('quase queimada')

else:
    print('queimou!')
    


    