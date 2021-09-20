// Wypisz zestawienie temperatur Far-Cel dla f =0,20,40,...,300
#include <stdio.h>

int main () {
    for(int i=0; i<= 300; i+=20){
        int cel = (i+32)/(1.8);
        printf("%d \n", cel);
    }
}
