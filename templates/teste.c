#include <stdio.h>
#include <stdlib.h>


typedef struct celula{
    int n;
    struct celula *prox;
} celula;

void adicionaFila(int n, celula *fila){
    celula *novo = malloc(sizeof(celula));
    novo->prox = fila->prox;
    novo->n = n;
    fila->prox = novo;
    return;
}

int main(void)
{   
    celula *fila = malloc(sizeof(celula));
    fila->prox = NULL;
    int *v = malloc(sizeof(int) * 10000);
    int contador = 0;
    int limite = 10000;
    int minimo;
    int calculador = 0;
    int ultimo = 0;
    while(1){
        if(contador == limite){
            v = (int*) realloc(v, sizeof(int) * limite * 2);
            limite = limite * 2;
        }
        scanf("%d", &v[contador]);
        if(v[contador] == 0){
            break;
        }
        contador = contador + 1;
    }
    scanf("%d", &minimo);
    for(int i = 0; v[i] != 0; i++){
        if(v[i] == 0)
            break;
        if(calculador > minimo){
            adicionaFila(ultimo, fila);
            calculador = 0;
            i--;
        }else{
            calculador = calculador + v[i];
            ultimo = v[i];
        }
    }
    for(celula *suporte = fila; suporte != NULL; suporte = suporte->prox){
        if(suporte->n != 0)
            printf("%d\n", suporte->n);
    }
    return 0;
}