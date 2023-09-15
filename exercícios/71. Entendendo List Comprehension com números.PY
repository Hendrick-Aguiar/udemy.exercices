# LIST comprehension
    #mais simples de se escrever
    # utilizado quando precisa-se criar uma nova lista a partir de uma existente
    # [expressão for item in itens]
#valores = []
#for x in range(6):
 #   valores.append(x * 10)
valores = [x * 10 for x in range(6)]
print(valores)
