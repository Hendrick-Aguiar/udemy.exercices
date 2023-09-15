#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


    
letra = str(input('Digite uma letra'))
vogais = 'aeiou'

def letras_vogal(letra, vogal):
    
if letra in vogais or vogais.upper():
    print('Vogal')
else:
    print('consoante')

letras_vogal()