try:
    valor = int(input('digite o valor do seu produto'))

    print(valor)
except ValueError:
    print('digite ovalor em números')
else:
    print('usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
finally:
    print('codigo ok')
    