ingredientes = ['trigo', 'fermento', 'leite', 'manteiga']#faça um bolo simples
print(ingredientes)
print('Insira os ingredientes acima na respectiva ordem para fazer o bolo: ')
ingrediente1 = str(input('insira o primeiro ingrediente: '))
ingrediente2 = str(input('insira o segundo ingrediente: '))
ingrediente3 = str(input('insira o terceiro ingrediente: '))
ingrediente4 = str(input('insira o quarto ingrediente: '))
bolo = [ingrediente1, ingrediente2, ingrediente3, ingrediente4]
if bolo == ingredientes:
    print('Parabens seu bolo estará pronto em 1 hora')
else:
    print('ingredientes incorretos')

