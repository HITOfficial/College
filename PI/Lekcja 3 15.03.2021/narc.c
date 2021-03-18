// Napisz program, który znajduje wszystkie liczby m-narcystyczne o bazie b.
#include <stdio.h>
#include <math.h>
#include <string.h>
// m <- ilość cyfy w liczbie
// b <- podstawa po konwersji

int sysToDec(int n, int b){ // number, base
    int p = 0; // power
    int d = 0;
    while(n > 0){
        d += (n%10)*pow(b,p);
        p+=1;
        n /=10;
    }
    return d;
}


char numberAsChar(int n){
    if(n>=0 && n <=9){
        return n+'0'; // zwracam jako stringa wartość
    }
    char T[6] = {'A','B','C','D','E','F'};
    return T[n%10];
}


int decToSys(int n,int b, int m){ // number, base, digits
    char T[m];
    int i = m -1; // zeby nie robic revers Tablicy wypełniam ją od końca
    while(n > 0){
        T[i] = numberAsChar(n%b);
        n /= b;
        i -= 1;
    }
    for(int i=0; i<m+1; i++){
        printf("%c",T[i]);
    }
    printf(" "); // odstep pomiedzy kolejnymi znalezionymi liczbami
    return 1;
}


int isNarc(int n, int b,int m) { // number, base, digits
    int n_sum = 0;
    while(n > 0){
        n_sum += pow(n%b,m);
        // if (pow(n%b,m) == 0){
        //     n_sum += 1;
        // }
        n /= b; 
    }
    return n_sum;
}



/// FFF(hex) = (2^4)*(2^4)*(2*4)-1 = 16^3
int maxNumber(int system, int digits){
    return pow(system, digits)-1;
}
int minNumber(int system, int digits){
    return pow(system,digits-1);
}


int main(void){
    int m,b;
    scanf("%d %d", &m, &b);
    // m = 3;
    // b = 11;
    int flag = 0;
    for(int i=minNumber(b,m); i<=maxNumber(b,m); i++){
        if(isNarc(i,b,m) == i){ // podana liczba jest narcystyczna
            decToSys(i, b, m);
            flag = 1;
        }
    }
    if(flag == 0){
        printf("NO");
    }
    // printf("%d",isNarc(126,11,3));
}
