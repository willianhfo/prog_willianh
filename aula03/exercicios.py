"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""


def soma_contando(lista):
   soma = 0
   operadores = 0
   n 
   for n in lista:
    soma = soma + operadores + 1
   return soma, operadores 

def busca_linear_contando(lista, alvo):
    comparacoes = 0
    n
    for n in range(len(lista)):
       comparacoes += 1
       if lista[n] == alvo:
          return n, comparacoes
    return (-1, comparacoes)
       
       


def busca_binaria_contando(lista, alvo):
     inicio = 0
     fim = len(lista) - 1
     comparacoes = 0
     while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == alvo:
           return (meio, comparacoes)
        elif lista[meio] < alvo:
           inicio = meio + 1
        else:
           fim = meio -1
     return (-1, comparacoes)

def tem_repetido_contando(lista):
    comparacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] == lista[j]:
                return (True, comparacoes)         
    return (False, comparacoes)



def quantas_divisoes(n):
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes += 1
    return divisoes


def mais_frequente_contando(lista):
    comparacoes = 0
    max_frequencia = 0
    elemento_mais_frequente = None
    n = len(lista)
    
    if n == 0:
        return (None, 0)
        
    for i in range(n):
        frequencia_atual = 1
        
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] == lista[j]:
                frequencia_atual += 1
                
        if frequencia_atual > max_frequencia:
            max_frequencia = frequencia_atual
            elemento_mais_frequente = lista[i]
            
    return (elemento_mais_frequente, comparacoes)
