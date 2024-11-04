# 1. bubbleSort
def bubbleSort (vetor):

    # for para contar as passagens pelo vetor
    # n rebe o tam do vetor, para qnd chegar em 0, e decresce de 1 em 1
    for i in range(len(vetor)):
        #for para andar pelas posições do vetor
        for j in range(0, len(vetor) - i - 1):
            if vetor[j] > vetor[j+1]:
                # trocando as posjções dos elementos
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return(vetor)


# 2. Bubble Sort Melhorado
def bubbleSortMelhorado (vetor):
    
    # controla o número de varreduras
    for i in range(len(vetor)):
        ocorreuTroca = False

        # percorre pelo vetor
        for j in range(len(vetor) - 1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                ocorreuTroca = True

        if not ocorreuTroca:
            return (vetor)
        
    return(vetor)


# 3. Quick Sort
# função auxiliar pra trocar dois elementos
def troca (arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# função de partição do quick sort
def particaoQuick (arr, esq, dir):
    
    # o pivô é o primeiro elemento
    pivo = arr[esq]

    # define um índice após o pivô, que vai da esq para a dir
    i = esq + 1
    # define um índice que vai da dir para a esq
    j = dir

    # loop infinito que para quando os índices se cruzam
    # verificando que encontrou valores que podem ser trocados
    while True:

        # move o i para até encontrar um valor da esq que seja maior que o pivo
        while i <= j and arr[i] < pivo:
            i += 1
        
        # move o j até encontrar um valor menor que o pivo
        while i <= j and arr[j] >= pivo:
            j -= 1


        # se encontrou elementos para trocar, realiza essa troca
        if i <= j:
            troca(arr, i, j)
        else:
            break

    # coloca o pivo na posição correta
    troca (arr, esq, j)
    # esse índice será usado para dividir o array em duas partes
    return j

def quickSort (arr):

    # inicializa a pilha com o intervalo (primeiro elemento, e último elemento)
    pilha = [(0, len(arr) -1)]

    # inicia um loop que continua até que a pilha esteja vazia
    while pilha:

        # remove o par de índices do topo da pilha e atribui esq ao inicio e dir ao fim do arr
        esq, dir = pilha.pop()

        # verifica se o intervalo tem mais de um elemento (se não ele já está ordenado)
        if esq < dir:
            # chama a função para organizar o subarray 
            pivo = particaoQuick(arr, esq, dir)

            # se a esq tiver mais de um elemento, aciona esse intervalo à pilha pra processar mais tarde
            if pivo - 1 > esq:
                pilha.append((esq, pivo - 1))

            # da mesma forma tbm adiciona esse intervalo à pilha
            if pivo + 1 < dir:
                pilha.append((pivo + 1, dir))
    

    return arr


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

    return (vetor)

# 5. Insertion Sort
def insertionSort (vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        
        vetor[j + 1] = chave

    return (vetor)

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

    return (vetor)


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
    
    return (vetor)

# 8. Heap Sort
def peneira (vetor, raiz, fundo):
    pronto = False
    while (raiz*2 <= fundo) and not pronto:
        if raiz*2 == fundo:
            filhoMax = raiz * 2
        elif vetor[raiz * 2] > vetor[raiz * 2 + 1]:
            filhoMax = raiz * 2
        else:
            filhoMax = raiz * 2 + 1
        
        if vetor[raiz] < vetor[filhoMax]:
            vetor[raiz], vetor[filhoMax] = vetor[filhoMax], vetor[raiz]
            raiz = filhoMax
        else:
            pronto = True
            

def heapSort (vetor):
    tam = len(vetor)

    for i in range(tam // 2, -1, -1):
        peneira(vetor, i, tam -1)
    
    for i in range(tam - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        peneira(vetor, 0, i - 1)
    
    return (vetor)


# 9. Merge Sort 
def merge(subVetor, auxVetor, ini, meio, fim):
    i = ini
    j = meio
    k = ini  # Começar a partir de 'ini'

    # Mescla os dois subvetores
    while i < meio and j < fim:
        if subVetor[i] <= subVetor[j]:
            auxVetor[k] = subVetor[i]
            i += 1
        else:
            auxVetor[k] = subVetor[j]
            j += 1
        k += 1

    # Copia os elementos restantes do primeiro subvetor, se houver
    while i < meio:
        auxVetor[k] = subVetor[i]
        i += 1
        k += 1

    # Copia os elementos restantes do segundo subvetor, se houver
    while j < fim:
        auxVetor[k] = subVetor[j]
        j += 1
        k += 1

    # Copia o vetor ordenado de volta para o vetor original
    for k in range(ini, fim):
        subVetor[k] = auxVetor[k]


def mergeSort(vetor, ini, fim):
    
    if ini < fim - 1:
        meio = (ini + fim) // 2


        # Metade da esquerda - dividir
        mergeSort(vetor, ini, meio)
        # Metade da direita - dividir
        mergeSort(vetor, meio, fim)
        # Função que aplica o merge - juntar os elementos
        merge(vetor, [0] * len(vetor), ini, meio, fim)
    
    return (vetor)


