#atravez do import posso chamar a função de outro arquivo
#import funcoes
#atravez do from podemos chamar um arquivo 
# escolher uma ou mais funções contidas nele
#podemos também usar asterico * para chamar todas as funções 
from funcoes import soma, mult

#arquivo/função
#funcoes.soma()
#funcoes.mult()
# aqui podemos organizar por arquivos criando pastas inserindo 
# __init__.py
from itens.cadastro import cliente

soma()
mult()
cliente()