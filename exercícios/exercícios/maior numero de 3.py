
#Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input('insira o numero'))
num2 = int(input('insira o numero'))
num3 = int(input('insira o numero'))

if (num1>num2 and num1>num3):
    print('o maior numero é', num1)
elif (num2>num3):
    print('o maior numero é', num2)
else:
    print('o maior numero é o numero', num3)
python -m pip install -U "watchdog[watchmedo]"