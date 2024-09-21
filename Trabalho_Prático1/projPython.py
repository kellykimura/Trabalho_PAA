# 1. bubbleSort
def bubbleSort (vetor):

    # for para contar as passagens pelo vetor
    # n rebe o tam do vetor, para qnd chegar em 0, e decresce de 1 em 1
    for i in range(len(vetor) -1, 0, -1):

        #for para andar pelas posições do vetor
        for j in range(i):
            if vetor[j] > vetor[j+1]:
                # trocando as posjções dos elementos
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# como chamar
# bubbleSort(vetor)


# 2. Bubble Sort Melhorado
def bubbleSortMelhorado (vetor):
    
    for i in range(1, len(vetor), 1):
        swapped = False

        for j in range(len(vetor) - 1 - i):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                swapped = True

            if not swapped:
                break


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
        
        

vetor = [5, 2, 9, 13, 1, 23, 45, 3, 8, 6]
#bubbleSort(vetor)
#bubbleSortMelhorado(vetor)

quickSort(vetor, 0, len(vetor) - 1)
print(vetor)

