# 1. bubbleSort
def bubbleSort (vetor):

    # for para contar as passagens pelo vetor
    # n rebe o tam do vetor, para qnd chegar em 0, e decresce de 1 em 1
    for n in range(len(vetor) -1, 0, -1):

        #for para andar pelas posições do vetor
        for i in range(n):
            if vetor[i] > vetor[i+1]:
                swapped = True
                # trocando as posições dos elementos
                vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

# como chamar
# bubbleSort(vetor)


