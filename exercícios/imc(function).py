

# < menor
# > maior




altura = float(input('insira a altura em metros: '))
peso = float(input('insira a altura em kg: '))



    
imc = peso / (altura ** 2 )

if imc < 18.5:
    print('muito magro')
elif imc >=18.5 and imc < 24.9:
    print('peso normal')
elif imc >=25 and imc <29.9:
    print('sobrepeso')
elif imc >=30 and imc < 39.9:
    print('obesidade')
