#calculadora de tintas: funções





rendimento = int(input('Qual o rendimento da Lata? '))

altura = int(input('qual a altura?'))

largura = int(input('qual a largura?'))

def quantidade_latas():
    m2 = altura * largura
    total = m2/rendimento
    print(f'O numero de latas de tinta é latas {total} latas')

quantidade_latas()






    









