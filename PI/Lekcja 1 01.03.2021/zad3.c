//  erastotenes sieve
#include <stdio.h>

int main(){
    int T[1001];
    for(int i=0; i<=1000; i+= 1){
        T[i] = i;
    }
    int ErastotenesNumbers[4] = {2,3,5,7};
    for(int j=0; j<4; j++){
        for(int i=2; i*ErastotenesNumbers[j] < sizeof(T)/sizeof(*T); i++){
            T[ErastotenesNumbers[j] * i] = 0;
        }
    }
    for(int i = 0; i < sizeof(T)/sizeof(*T); i++){
        if(T[i] != 0){
            printf("%d\n",T[i]);
        }
    }
}