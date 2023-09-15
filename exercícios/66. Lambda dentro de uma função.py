#66. Lambda dentro de uma função
#transforma a função com vários argumentos com somente 1 função
#tendo assim um código mais clean
def somar(x):
    func2 = lambda x: x+10
    return func2(x) * 4
print(somar(2))