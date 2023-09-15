#while loop ===
# excelente para loops 
# dependentes de uma condição.
#criar um promoção para um produto no valor de R$ 100.

valor = 100
dia = 0
while valor > 20:
    dia += 1
    print(f' no dia{dia} o produto será vendido R$ {valor}')
    
    valor -= 5