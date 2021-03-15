// Napisz program, który przyjmuję tablicę liczb naturalnych i zwraca taki indeks, że sumy
// wartości elementów tablicy na lewo i na prawo od wyznaczonego miejsca są równe. Można
// założyć, że rozwiązanie istnieje.

// n -> dł tablicy
// elementy tablicy po spacji

#include <stdio.h>


int indexOfEq(int *T, int limit, int n){ // tablica, dł. tablicy
    int sumLeft = 0;
    int sumRight = 0;
    for(int i=0; i<limit; i++){
        sumLeft += T[i];
    }
    for(int i=n-1; i>limit; i--){
        sumRight += T[i];
    }
    if (sumLeft == sumRight){
        return 1;
    }
    return 0;
}

int main(void){
    int n;
    scanf("%d",&n);
    int T[n];
    for(int i=0; i<n; i++){
        scanf("%d", &T[i]);
    }
    for(int i=1; i<n-1; i++){
        if(indexOfEq(T,i,n)==1){ // znaleziono
            printf("%d ",i);
        }
    }
}

