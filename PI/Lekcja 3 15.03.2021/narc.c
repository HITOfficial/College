// Napisz program, który znajduje wszystkie liczby m-narcystyczne o bazie b.
#include <stdio.h>
#include <math.h>



int systemToDec(int num,int sys){
    if (sys == 10){
        return num;
    }
    int dec_sum = 0;
    int power = 0;
    while(num > 0){
        dec_sum += (num%10) * pow(sys,power);
        power += 1;
        num /=10;
    }
    return dec_sum;
}



int main(void){
    int m, b; // digits in number system
    // scanf("%d %d", &m, &b);
    m = 122;
    b = 3;
    int x = systemToDec(m,b);
    printf("%d", x);
}