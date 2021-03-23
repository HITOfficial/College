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


int digitsSquares(int n){
    int squareSum = 0;
    while(n > 0){
        squareSum += (n%10) * (n%10);
        n = floor(n/10);
    }
    return squareSum;
}


int main(void){
    int counter = 0;
    int L, U, K;
    scanf("%d %d %d", &L, &U, &K);
    for(int i=L+1; i<U; i++){
        if(isprime(i)==1){
            int squares = 0;
            int flag = 0;
            int j = i;
            while(squares < 10){
                j = digitsSquares(j);
                if(j == 1){
                    counter += 1;
                    if(counter == K){
                        flag = 1;
                        printf("%d ",i);
                        break;
                    }
                    break;
                }
                squares +=1;
            }
            if(flag == 1){
                break;
            }
        }
    }
    if(counter<K){
        printf("%d",-1);
    }
}
