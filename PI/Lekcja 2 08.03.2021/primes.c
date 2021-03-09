// Dana jest liczba całkowita dodatnia n. Napisz program, który znajduje wszystkie liczby
// pierwsze mniejsze od n, których cyfry tworzą ciąg niemalejący.
#include <stdio.h>

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


int ascending(int n){
    int last = n%10;
    n /=10;
    while(n > 0){
        if(last >= n%10){
            last = n%10;
            n /= 10;
        }
        else{
            return 0;
        }
    }
    return 1;
}


int main(void){
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        if(isprime(i)==1){
            if(ascending(i)==1){
                printf("%d\n",i);
            }
        }
    }
}
    