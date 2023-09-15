# armazenar mais de uma informação me variáveis
# manter a sequencia dos dados em uma variável
# usando  a função lower() case que aceita letras maiúsculas e min
cores_cliente = input('digite a cor desejada: ')
cores = ['amarelo','verde', 'azul','vermelho']

if cores_cliente.lower() in cores:
    print('temos em estoque')
else:
    print('não temos em estoque')