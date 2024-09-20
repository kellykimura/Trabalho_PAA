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

void bubbleSortMelhorado(int *vetor, int tamanhoVetor){
     int i, j, aux, ocorreuTroca;
    for (i = 1; i < tamanhoVetor; i++){         //Controla o numero de varreduras
        ocorreuTroca = 0; //Não ocorreu troca
        for (j = 0; j < tamanhoVetor-1; j++){   // Aponta para as posicoes do vetor

            if (*(vetor+j) > *(vetor+j+1)){  //Permutando elementos
                aux =  *(vetor+j);
                *(vetor+j) = *(vetor+j+1);
                *(vetor+j+1) = aux;
                ocorreuTroca = 1; //Ocorreu troca
            }
        } //Fim for interno
        if(ocorreuTroca == 0) return;//Não ocorreu troca
    } //Fim for externo
    return;
}

void quickSort(){

}

void quickSortMelhorado();

void insertionSort(int *vetor, int tamanhoVetor){
    int i, j, chave;

    for (i = 1; i < tamanhoVetor; i++){       // controla o numero de varreduras que deve ser (Tamanho-1)
        chave = *(vetor+i);
        j = i-1;
        while ((j >= 0) && (*(vetor+j) > chave)){   // procura a posição correta para inserir o elemento chave
            *(vetor+j+1) = *(vetor+j);  // deslocando o elemento e abrindo espaço para a futura inserção
            j--;
        }//Fim do while
        *(vetor+j+1) = chave; //Inserindo o elemento chave em sua posição correta
    }//Fim do for
    return;
}

void shellSort(){

}

void selectionSort(int *vetor, int tamanhoVetor){
    int i, j, menor, posMenor;
    for (i = 0; i < tamanhoVetor-1; i++){

        menor = *(vetor+i);
        posMenor = i;
        for (j = i+1; j < tamanhoVetor; j++){   //Encontrando o menor elemento e sua posição
            if (*(vetor+j) < menor){
                menor = *(vetor+j);
                posMenor = j;
            }
        } //Fim for interno
        *(vetor+posMenor) = *(vetor+i);
        *(vetor+i) = menor;
    } //Fim for externo
    return;
}

void heapSort(){

}

void mergeSort(){
    
}






int main()
{






    return 0;
}