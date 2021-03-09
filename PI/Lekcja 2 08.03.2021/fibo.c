// Napisz program, który dla zadanej liczby naturalnej n odpowiada na pytanie, czy liczba
// ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego. Zakładamy,
// że pierwsze dwa wyrazy ciągu Fibonacciego to 0 i 1.
#include <stdio.h>


int fibonacci(int n){
    int f1 = 0;
    int f2 = 1;
    if (f1*f2 == n){ // bo w while pomijam przypadek poczatkowy
        return 1;
    }
    while(f1*f2 <= n){
        int tmp = f2;
        f2 = f2 + f1;
        f1 = tmp;
        if(f1*f2 == n){
            return 1;
        }
    }
    return 0;
}

int main(void){
    int n;
    scanf("%d",&n);
    if(fibonacci(n) == 1){
        printf("YES");
    }
    else{
        printf("NO");
    }
}