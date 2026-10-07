"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    resultado = []
    for i in lista:
        if i >= 0:
            resultado.append(i)
    return resultado       
            


def inverte(lista):
    resultado = []
    j = len(lista)-1
while j >=0:
    resultado.append(lista(j))



def busca_binaria(lista, alvo):
    esq = 0
    dir = len(lista) - 1

    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        
        if lista[meio] < alvo:
            esq = meio + 1

        else:
            dir = meio - 1

        return -1



def intercala(lista_a, lista_b):
    intercalada = []
    for i in range(len(lista1)):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    return intercalada



def remove_repetidos(lista):
  removerepet = []

    for n in lista_original:

    if n not in removerepet:
        removerepet.append(numero)

    return removerepet


