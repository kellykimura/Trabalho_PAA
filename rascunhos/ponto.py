

def insertionSort (vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        
        vetor[j + 1] = chave

vetor = [5, 2, 9, 13, 1, 23, 45, 3, 8, 6]

insertionSort(vetor)
print(vetor)
