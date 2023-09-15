
# enviar um email com os detalhes da compra online (máximo 3
# tentativas) para compras confirmadas.
compra_confirmada = True
dados_compra = 'compra no valor de 12.50 e entrega confirmada'
if compra_confirmada:
    print(dados_compra)
    print('detalhes enviados para o seu email')

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes enviados para o seu email')
        break
else:
    print('falha na compra')
    