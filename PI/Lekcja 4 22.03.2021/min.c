#include <stdio.h>
#include <math.h>

int findMax(int *T,int n){
    int maximum = 0;
    for(int i=1; i<n; i++){
        if (T[i]>T[maximum]){
            maximum = i;
        }
    }
    return maximum;
}

// Tworze tablicę pomocniczą w której będę trzymał floor(wartości//2)
int main(void){
    // rozmiar, ilosc do podzialu
    // elementy
    int n,k;
    scanf("%d %d", &n,&k);
    int T[n];
    for(int i=0; i<n; i++){
        scanf("%d",&T[i]);
    }
    while(k > 0){
        int maxValIndex = findMax(T,n);
        // printf("%d, %d", maxValIndex, T[maxValIndex]/2);
        T[maxValIndex] = T[maxValIndex]/2;
        k -= 1;
    }
    int arrSum = 0;
    for(int i=0;i<n; i++){
        arrSum += T[i];
    }
    printf("%d",arrSum);
}

