#Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da
#mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
#papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

def verif(x):

    tam = len(x)

    if tam > 1:
        if x[0] == x[-1]:
            return verif(x[1:-2])
        else:
            return False
    else:
        return True

palavra = input("Palavra a verificar se é palindromo => ")

print (verif(palavra))