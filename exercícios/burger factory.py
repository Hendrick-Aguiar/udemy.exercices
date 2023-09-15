# sistema para fabricação de hamburguers
# o self fará o loop de todos os dados inseridos na função da classe contrutora
# que no caso é o __init__ por isso deve ser colocado primeiro


# agora precisa-se pássar os parâmentros 

#def exemplo(), print("oi"), etc 
# #lista = [1 , 2 , 3, "oi" ] <--- para uma lista
# dic = {"parenteses": "função", "colchetes":"lista", "chaves": "dicionário" } <--- para uma dicionário

class Burger:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    def print(self):
        print(self.ingredientes)

class Fabrica_hamburguer:
    
    def X_salada(self):
        ingredientes = ['carne', 'queijo', 'alface', 'tomate', 'cebola', 'ervilha', 'milho']
        return Burger(ingredientes)
    
    def X_filé(self):
        ingredientes = ['filé' 'mignion', 'alface', 'tomate', 'queijo']
        return Burger(ingredientes)

Fabrica_Hamburgueres = Fabrica_hamburguer()
Fabrica_Hamburgueres.X_salada().print()
Fabrica_Hamburgueres.X_filé().print()
        
        
       
        
         
        