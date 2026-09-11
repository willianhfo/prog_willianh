"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma
    

def conta_pares(lista):
    conta_pares = 0
    for i in lista:
        if (i % 2 == 0):
            conta_pares = conta_pares + 1
    return conta_pares
    

def maior_valor(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if maior < lista[i]:
            maior = lista[i]
    return maior        


def busca_linear(lista, alvo) :
    for i in range (len(lista)):
        if lista [i] == alvo:
            return i 
    return -1


def existe(lista, alvo):
    for i in lista:
        if i == alvo:
            return True   
    return False

def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1
    pass


def segundo_maior(lista):
    maior = lista[0]
    segundo_maior = lista[1]
    if maior < segundo_maior:
        temp = maior
        maior = segundo_maior
        segundo_maior = temp
    for n in lista[2:]:
        if n > maior:
            segundo_maior = maiormaior = n
        elif n > segundo_maior:
            segundo_maior = n
    return segundo_maior
    
