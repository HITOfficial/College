//  erastotenes sieve
#include <stdio.h>

int main () {
    printf("%d\n hello");
    int T[20];
    for(int i =0; i<=1000; i+= 1){
        T[i] = i;
    }
    int number = 2;
    for(int i=2; i*number < sizeof(T)/sizeof(T[0]); i++){
        T[i*number] = 0;
    }
    number = 3;
    for(int i=2; i*number < sizeof(T)/sizeof(T[0]); i++){
        T[i*number] = 0;
    }
    number = 5;
    for(int i=2; i*number < sizeof(T)/sizeof(T[0]); i++){
        T[i*number] = 0;
    }
    number = 7;
    for(int i=2; i*number < sizeof(T)/sizeof(T[0]); i++){
        T[i*number] = 0;
    }
    for(int i = 0; i < sizeof(T)/sizeof(T[0]); i++){
        if(T[i] != 0)
            printf("%d\n",T[i]);
    }
}