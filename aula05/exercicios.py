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
