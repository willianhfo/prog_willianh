"""Lista B - ordenacao, dois indices e janela, contagem por chave.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Nos exercicios de ordenacao, NAO use sorted() nem list.sort().
Onde o enunciado pede lista nova, preserve a lista recebida.
bubble_sort e selection_sort devolvem (lista_ordenada, comparacoes, trocas),
o mesmo contrato da aula05.
"""

# ---------- Bloco 1: ordenacao ----------

def passagem_bubble(lista):
     resultado = list(lista)
    n = len(resultado)
    for i in range(n - 1):
        if resultado[i] > resultado[i + 1]:
            resultado[i], resultado[i + 1] = resultado[i + 1], resultado[i]
    return resultado


def bubble_sort(lista):
    resultado = list(lista)
    n = len(resultado)
    comparacoes = 0
    trocas = 0
    for fim in range(n - 1, 0, -1):
        trocou = False
        for i in range(fim):
            comparacoes += 1
            if resultado[i] > resultado[i + 1]:
                resultado[i], resultado[i + 1] = resultado[i + 1], resultado[i]
                trocas += 1
                trocou = True
        if not trocou:
            break
    return resultado, comparacoes, trocas



def selection_sort(lista):
    resultado = list(lista)
    n = len(resultado)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if resultado[j] < resultado[min_idx]:
                min_idx = j
        if min_idx != i:
            resultado[i], resultado[min_idx] = resultado[min_idx], resultado[i]
            trocas += 1
    return resultado, comparacoes, trocas



def insertion_sort(lista):
    resultado = list(lista)
    for i in range(1, len(resultado)):
        chave = resultado[i]
        j = i - 1
        while j >= 0 and resultado[j] > chave:
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = chave
    return resultado


def quicksort(lista):
    if len(lista) <= 1:
        return list(lista)
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)



# ---------- Bloco 2: dois indices e janela ----------

def eh_palindromo(texto):
    esq = 0
    dir = len(texto) - 1
    while esq < dir:
        if texto[esq] != texto[dir]:
            return False
        esq += 1
        dir -= 1
    return True


def par_que_soma(lista, alvo):
    esq = 0
    dir = len(lista) - 1
    while esq < dir:
        soma = lista[esq] + lista[dir]
        if soma == alvo:
            return (esq, dir)
        if soma < alvo:
            esq += 1
        else:
            dir -= 1
    return (-1, -1)


def remove_repetidos_ordenada(lista):
    if not lista:
        return []
    resultado = [lista[0]]
    for item in lista[1:]:
        if item != resultado[-1]:
            resultado.append(item)
    return resultado



def soma_maxima_janela(lista, k):
    soma_atual = sum(lista[:k])
    maior_soma = soma_atual
    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > maior_soma:
            maior_soma = soma_atual
    return maior_soma


def conta_janelas_acima(lista, k, limite):
    soma_atual = sum(lista[:k])
    contador = 1 if soma_atual > limite else 0
    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > limite:
            contador += 1
    return contador


# ---------- Bloco 3: contagem por chave ----------

def conta_frequencias(lista):
    freq = {}
    for item in lista:
        freq[item] = freq.get(item, 0) + 1
    return freq


def mais_frequente(lista):
    freq = conta_frequencias(lista)
    melhor_item = lista[0]
    maior_freq = freq[melhor_item]
    for item in lista:
        if freq[item] > maior_freq:
            maior_freq = freq[item]
            melhor_item = item
    return melhor_item


def primeiro_unico(lista):
    freq = conta_frequencias(lista)
    for item in lista:
        if freq[item] == 1:
            return item
