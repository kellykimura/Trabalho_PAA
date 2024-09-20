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

def bubbleSortMelhorado (vetor):
    
    for i in range(1, len(vetor), 1):
        swapped = False

        for j in range(len(vetor) - 1 - i):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                swapped = True

            if not swapped:
                break

vetor = [5, 2, 9, 1, 8, 6]
bubbleSort(vetor)
#bubbleSortMelhorado(vetor)
print(vetor)

