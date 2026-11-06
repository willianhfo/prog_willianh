"""Aula 04 - Por que ordenar?

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Hoje voce NAO escreve algoritmo de ordenacao. Use sorted(lista), que
devolve uma lista nova e ordenada sem mexer na original. Evite lista.sort(),
que altera a lista de quem chamou a funcao.
"""


def custo_binaria(n):
    """PRONTA. Nao mexa.
    Pior caso da busca binaria numa lista de n elementos.
    E a quantas_divisoes da aula passada mais 1."""
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes = divisoes + 1
    return divisoes + 1


def tem_repetido_ordenando(lista):
    copia = sorted(lista)
    comparacoes = 0
    for i in range(len(copia) - 1):
        comparacoes += 1
        if copia[i] == copia[i + 1]:
            return (True, comparacoes)
    return (False, comparacoes)



def mediana(lista):
    if not lista:
        return None
    copia = sorted(lista)
    n = len(copia)
    meio = n // 2
    if n % 2 != 0:
        return copia[meio]
    else:
        return (copia[meio - 1] + copia[meio]) / 2.0


def buscas_para_compensar(n, custo_ordenar):
    if n <= 0:
        return -1
    c_bin = custo_binaria(n)
    if c_bin >= n:
        return -1
    ganho_por_busca = n - c_bin
    k = (custo_ordenar // ganho_por_busca) + 1
    return k





def menor_diferenca(lista):
    if len(lista) < 2:
        return None
    copia = sorted(lista)
    min_dif = copia[1] - copia[0]
    for i in range(1, len(copia) - 1):
        dif = copia[i + 1] - copia[i]
        if dif < min_dif:
            min_dif = dif
    return min_dif

