// Liczba doskonała to liczba naturalna, która jest sumą wszystkich swych dzielników właściwych (to znaczy od niej mniejszych). Najmniejszą liczbą
// doskonałą jest 6=3+2+1. Następną jest 28=14+7+4+2+1. Znajdź liczby doskonałe w zadanym przedziale [0, 10000]
#include <stdio.h>

int main(){
    for(int i=1; i<=1000; i+=1){
        int valuesSum = 0;
        for(int j=1; j<i; j+=1){
            if(i%j == 0)
                valuesSum += j;
        }
        if(valuesSum == i)
            printf("%d \n", i);
    }

}