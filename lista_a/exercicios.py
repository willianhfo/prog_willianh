"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador



def media(lista):
    if len(lista) == 0: 
        return 0
    return sum(lista) / len(lista)



def sem_o_maior(lista):
    if len(lista) == 0:
        return []
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    nova = []
    ja_tirou = False
    for n in lista:
        if n == maior and ja_tirou == False:
            ja_tirou = True
        else:
            nova.append(n)
    return nova




def acumulada(lista):
    nova = []
    soma_atual = 0
    for n in lista:
        soma_atual += n
        nova.append(soma_atual)
    return nova



def achata(lista_de_listas):
    nova = []
    for sublista in lista_de_listas:
        for elemento in sublista:
            nova.append(elemento)
    return nova



# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i
    return -1



def conta_ocorrencias(lista, alvo):
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return contador



def primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    posicao_encontrada = -1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == alvo:
            posicao_encontrada = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return posicao_encontrada



# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    soma_pares = 0
    operacoes = 0
    for numero in lista:
        operacoes += 1
        if numero % 2 == 0:
            soma_pares += numero
    return (soma_pares, operacoes)



def maior_contando(lista):
    maior = lista[0]
    comparacoes = 0
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
    return (maior, comparacoes)



def tem_soma_contando(lista, alvo):
    comparacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return (True, comparacoes)
    return (False, comparacoes)



def ordenada_contando(lista):
    comparacoes = 0
    if len(lista) < 2:
        return (True, comparacoes)
    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return (False, comparacoes)
    return (True, comparacoes)



# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1



def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1
    return True



def par_que_soma(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio < fim:
        soma_atual = lista[inicio] + lista[fim]
        if soma_atual == alvo:
            return (inicio, fim)
        elif soma_atual < alvo:
            inicio += 1
        else:
            fim -= 1   
    return (-1, -1)



def soma_maxima_janela(lista, k):
    if not lista or k <= 0 or len(lista) < k:
        return 0
    soma_atual = sum(lista[:k])
    max_soma = soma_atual
    for i in range(k, len(lista)):
        soma_atual = soma_atual + lista[i] - lista[i - k]
        if soma_atual > max_soma:
            max_soma = soma_atual
    return max_soma



def parenteses_balanceados(texto):
    pilha = []
    pares = {")": "(", "]": "["}
    
    for caractere in texto:
        if caractere in "([":
            pilha.append(caractere)
        elif caractere in ")]":
            if not pilha or pilha[-1] != pares[caractere]:
                return False
            pilha.pop()
    return len(pilha) == 0

