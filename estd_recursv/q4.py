# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem crescente.

def imprime(inicio, limite):
    
    if inicio <= limite:
        print(inicio)
        imprime(inicio+1, limite)


n = int(input("Digite um valor inteiro positivo => "))

imprime(0, n)