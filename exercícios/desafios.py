cozimento = int(input('Insira a temperatura '))

if cozimento < 48:
    print('está crua')
    
elif cozimento in range(48, 53):
    print('mal passada')
elif cozimento in range(54, 60):
    print('no ponto')
elif cozimento in range(61, 70):
    print('bem passada')
elif cozimento in range(71, 80):
    print('muito assada')
elif cozimento >= 90:
    print('queimada')    
