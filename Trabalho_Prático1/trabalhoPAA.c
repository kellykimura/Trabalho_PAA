/*
Bubble Sort (versão original sem melhorias—não verificar se o vetor já está ordenado)
Bubble Sort melhorado (verifica se o vetor já está ordenado)
Quick Sort (com pivô sendo o primeiro elemento da lista—partição)
Quick Sort (com pivô sendo o elemento central da lista—partição)
Insertion Sort (inserção simples ou inserção direta)
Shell Sort
Selection Sort (Seleção Direta)
Heap Sort
Merge Sort
*/

#include<stdio.h>
#include<stdlib.h>

void bubbleSort(int *vetor, int tamanhoVetor){
    int i, j, aux;
    for (i = 1; i < tamanhoVetor; i++){         //Controla o numero de varreduras
        for (j = 0; j < tamanhoVetor-1; j++){   // Aponta para as posicoes do vetor

            if (*(vetor+j) > *(vetor+j+1)){  //Permutando elementos
                aux = *(vetor+j);
                *(vetor+j) = *(vetor+j+1);
                *(vetor+j+1) = aux;
            }
        } //Fim for interno
    } //Fim for externo
    return;
}

void bubbleSortMelhorado(){
    
}

void quickSort();

void quickSortMelhorado();

void insertionSort();

void shellSort();

void selectionSort();

void heapSort();

void mergeSort();






int main()
{






    return 0;
}