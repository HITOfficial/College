// 1 Zadanie
// Liczba doskonała jest to taka liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od niej mniejszych). Najmniejszą liczbą doskonałą jest 6,
// ponieważ jej dzielnikami właściwymi są 1, 2, 3 i 1 + 2 + 3 = 6.
// Napisz program, który znajduje wszystkie liczby doskonałe w zadanym przedziale oraz
// ich liczbę.
// 2 Wejście
// Pierwszy i jedyny wiersz standardowego wejścia zawiera dwie liczby naturalne 1 ¬ m, n ¬
// 108
// , będące odpowiednio początkiem i końcem przedziału.
// 3 Wyjście
// W pierwszym wierszu standardowego wyjścia powinna znaleźć się jedna liczba całkowita
// p: liczba znalezionych liczb doskonałych. Drugi wiersz zawiera dokładnie p liczb całkowitych: znalezione liczby doskonałe w porządku rosnącym.
#include <stdio.h>

int main(void){
    int T[15];
    int m, n;
    int p = 0;
    int id = 0;
    scanf("%d %d", &m, &n);
    for(m;m<=n; m++){
        int sum = 0;
        for(int j=1; j<=m/2; j++){
            if(m%j== 0){
                sum+=j;
            }
        }
        if(m == sum){
            T[id] = m;
            id += 1;
            p+=1;
        }
    }
    printf("%d\n", p);
    for(int i=0; i<id; i++){
        printf("%d ",T[i]);
    }
}
