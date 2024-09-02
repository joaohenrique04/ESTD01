# Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1

def fat(x):

    print(x, end=" ")
    if x != 1:
        print("*", end=" ")
        return x * fat(x-1)
    else:
        print("=")
        return 1

# entrada de dados
vlr = int(input("Digite o numero para obter o fatorial => "))

# r vai retornar o valor final
r = fat(vlr)

# impressao do valor final
print(r)