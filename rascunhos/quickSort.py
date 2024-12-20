# 3. Quick Sort
def particaoQuickSort (vetor, esquerda, direita):
    pivo = vetor[esquerda]
    i = esquerda + 1
    j = direita

    while i <= j:

        while i <= direita and vetor[i] <= pivo:
            i += 1

        while j >= esquerda and vetor[j] > pivo:
            j -= 1

        if i < j:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
            j -= 1
        
    
    vetor[esquerda], vetor[j] = vetor[j], vetor[esquerda]
    return j

def quickSort (vetor, esquerda, direita):
    if esquerda < direita:
        meio = particaoQuickSort(vetor, esquerda, direita)
        quickSort(vetor, esquerda, meio - 1)
        quickSort(vetor, meio + 1, direita)


# 4. Quick Sort Melhorado
# precisa desta função para o QuickSortMelhorado
def particaoQuickSortMelhorado (esq, dir, vetor):
    i = esq
    j = dir
    pivo = vetor[(i + j) // 2]

    while i <= j:
        while pivo > vetor[i]:
            i += 1
        while pivo < vetor[j]:
            j -= 1
        if i <= j:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
            j -= 1
    
    return i, j

#precisa desta função para o QuickSortMelhorado 
def ordena (esq, dir, vetor):
    i, j = particaoQuickSortMelhorado(esq, dir, vetor)
    
    # chama recursivamente para o lado esquerdo da partição
    if esq < j:
        ordena(esq, j, vetor)

    # chama recursivamente para o lado direito da partição
    if i < dir:
        ordena(i, dir, vetor)

def quickSortMelhorado(vetor):
    ordena(0, len(vetor)-1, vetor)