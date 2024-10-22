import random

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

# 5. Insertion Sort
def insertionSort (vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        
        vetor[j + 1] = chave

# 6. Shell Sort
def shellSort (vetor):
    tam = len(vetor)
    h = 1
    while h < tam:
        h = 3 * h + 1
    
    while h > 1:
        h //= 3
        for i in range(h, tam):
            tmp = vetor[i]
            j = i - h
            while j >= 0 and tmp < vetor[j]:
                vetor[j + h] = vetor[j]
                j -= h
            vetor[j + h] = tmp


# 7. Selection Sort
def selectionSort (vetor):
    tam = len(vetor)
    for i in range (tam - 1):
        menor = vetor[i]
        posMenor = i
        for j in range (i + 1, tam):
            if vetor[j] < menor:
                menor = vetor[j]
                posMenor = j

        vetor[posMenor], vetor[i] = vetor[i], menor

# 8. Heap Sort

# 9. Merge Sort 


vetor = [12, 14, 15, 88, 203, 789, 5, 2, 9, 13, 1, 23, 45, 3, 8, 6, 27, 109, 4, 7, 11, 10, 21]
#bubbleSort(vetor)
#bubbleSortMelhorado(vetor)

for _ in range(5):
  vetor = random.randint(1, 100)
  


quickSort(vetor, 0, len(vetor))
print(vetor)

