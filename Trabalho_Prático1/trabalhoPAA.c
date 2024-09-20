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

//para testar o caso médio
void inserirElementosOrdemAleatoria();

//para testar o melhor caso
void inserirElementosOrdemCrescente();

//para testar o pior caso
void inserirElementosOrdemDecrescente();


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

//precisa desta função para o QuickSort 
int particao(int *vetor, int esquerda, int direita){

	int pivo = *(vetor+esquerda), i = esquerda+1, j = direita, auxTroca;

	while(i <= j) {									    //Para o particionamento quando o lado esquerdo e direito se cruzarem.

		if(*(vetor+i) <= pivo) ++i;						//Avança a posição referente ao lado esquerdo.
		else if(pivo < *(vetor+j)) --j;					//Retrocede a posição referente ao lado direito.

		else{
			auxTroca = *(vetor+i);						//Troca os elementos de possição.
			*(vetor+i) = *(vetor+j);					//Troca os elementos de possição.
			*(vetor+j) = auxTroca;						//Troca os elementos de possição.
			++i, --j;
		}//Fim else
	}//Fim while

	*(vetor+esquerda) = *(vetor+j);
	*(vetor+j) = pivo;
	return j;										    //Retornando o valor de j.
}

void quickSort(int *vetor, int esquerda, int direita){
    if(esquerda < direita){						        //Para as chamadas recursivas quando o lado esquerdo e direito se cruzarem.
		int meio = particao(vetor,esquerda,direita);    //Particiona o vetor em duas partes utilizando pivo no inicio
		quickSort(vetor,esquerda,meio-1);			    //Aplica o Quick Sort na partição esquerda.
		quickSort(vetor,meio+1,direita);				//Aplica o Quick Sort na partição direita.
	}
	return;
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

//precisa desta função para o MergeSort
void merge(int *subVetor, int ini, int meio, int fim){
    int auxVetor[fim], i = ini, j = meio, k = ini;
    //i - contador da esq, j - contador da dir, k contador do auxVetor

    while((i<meio) && (j<fim)) { //Intercalando elementos para junção do subvetor
        if(*(subVetor+i) <= *(subVetor+j)){
            *(auxVetor+k) = *(subVetor+i);
            i++;
        }//Fim if
        else{
            *(auxVetor+k) = *(subVetor+j);
            j++;
        }//Fim else
        k++;
    }//Fim do while

    while(i<meio){*(auxVetor+k) = *(subVetor+i); k++; i++;}  //Copiando os elementos restantes (1ª metade/esquerda – se existirem)
    while(j<fim){*(auxVetor+k) = *(subVetor+j); k++; j++;}   //Copiando os elementos restantes (2ª metade/direita – se existirem)

    for (k = ini; k < fim; k++) {
        *(subVetor+k) = *(auxVetor+k); //Copiando os elementos já unidos e ordenados no subvetor (original)
    }
    return;
}

void mergeSort(int *vetor, int ini, int fim){
    if(ini < fim-1){
        int meio = (ini+fim)/2;

        mergeSort(vetor, ini, meio);	//Metade da esquerda - Dividir
        mergeSort(vetor, meio, fim);  //Metade da direita - Dividir
        merge(vetor, ini, meio, fim);   // função que aplica o merge, juntar os elementos - Conquistar
    }
}


int main()
{






    return 0;
}