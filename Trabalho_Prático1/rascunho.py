# quick Sort com pilha


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
    
    
    return(arr)
    



# Exemplo de uso
arr = [10, 11, 6, 17, 7, 8, 9, 1, 5, 12, 23, 34]
print(quickSort(arr))
