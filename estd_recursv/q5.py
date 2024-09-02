# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem decrescente.

def imprime(vlr):
    if vlr >= 0:
        print(vlr)
        imprime(vlr-1)


n = int(input("Digite um valor inteiro positivo => "))

imprime(n)