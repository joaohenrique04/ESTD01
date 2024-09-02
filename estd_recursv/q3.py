# Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
# ocorre 2 vezes em "estrutura"

def busca(p, c):

        if len(p) == 0:
            return 0

        c1 = p[0]
        novaPalavra = p[1:]

        if c1 == c:
            return(1+busca(novaPalavra, c))
        else:
            return(0+busca(novaPalavra, c))

palavra = input("Palavra a contar caractere => ")
caract  = input("Caractere a contar => ")

qtd = busca(palavra, caract)

print("Nº de Aparições:", qtd)