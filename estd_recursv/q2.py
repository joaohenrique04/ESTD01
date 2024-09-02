# Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

def inverte(p):
    
    tamanho = len(p)

    if tamanho > 0:
        print(p[-1], end="")
        nova = p[0:tamanho-1]
        inverte(nova)


palavra = input("Digite uma palavra para inverter => ")

inverte(palavra)