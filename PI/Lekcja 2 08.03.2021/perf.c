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
#include <math.h>

int isprime(int n){
    if(n <= 1){
        return 0;
    }
    if(n == 2 || n == 3){
        return 1;
    }
    if(n%2 ==0 || n%3 == 0){
        return 0;
    }
    int i = 5;
    while(i*i <= n){
        if(n%i == 0){
            return 0;
        }
        i+=2;
        if(n%i == 0){
            return 0;
        }
        i+=4;
    }
    return 1;
}


int main(void){
    int T[15];
    int m, n;
    int id = 0;
    int power = 0;
    int p = 0;

    scanf("%d %d", &m, &n);

    // metoda euklidesowa na podstawie Wiki

    while(pow(2,power+1) < n){ // na oko określam że 2^power+1 mniejsze od n (zaokrąglam 2^(k-1)*(2^k-1))
        if(isprime(pow(2,power)-1)){ // liczba (2^power)-1 pierwsza
            int k = (pow(2,power-1)*(pow(2,power)-1));
            if(k >= m && k <= n){
                T[id] = k;
                id +=1;
                p+=1;
            }
        }
        power +=1;
    }
    printf("%d\n", p);
    for(int i=0; i<id; i++){
        printf("%d ",T[i]);
    }
}
