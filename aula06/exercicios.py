def conta_frequencias(lista):
    freq = {}
    for item in lista:
        freq[item] = freq.get(item, 0) + 1
    return freq


def hash_soma(palavra, tamanho):
    return sum(ord(c) for c in palavra) % tamanho


def gavetas_com_colisao(palavras, tamanho):
    gavetas = {}
    for palavra in palavras:
        indice = hash_soma(palavra, tamanho)
        gavetas[indice] = gavetas.get(indice, 0) + 1
    return sum(1 for qtd in gavetas.values() if qtd > 1)


def mais_frequente(lista):
    freq = conta_frequencias(lista)
    melhor_item = lista[0]
    maior_freq = freq[melhor_item]
    for item in lista:
        if freq[item] > maior_freq:
            maior_freq = freq[item]
            melhor_item = item
    return melhor_item
