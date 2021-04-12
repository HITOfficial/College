// zrobić spirale
#include <stdio.h>

int main(void){
    int n, breakRow, breakCol;
    scanf("%d",&n);
    int Arr[n][n];
    int i = 0;
    int j = n-1;
    int value = 1;
    // dla parzystych i nieparzystych tablic inaczej sie zakancza
    // parzysta Arr[n//2][(n//2)-1]
    // nieparzysta Arr[n//2][n//2]
    if(n%2 == 0){
        breakRow = n/2;
        breakCol = (n/2)-1;
    }
    else{
        breakRow = n/2;
        breakCol = n/2;
    }

    while(i<j){
        for(int k=i;k<=j;k++){
            Arr[i][k] = value;
            value += 1;
        }
        i+= 1;
        for(int k=i;k<=j;k++){
            Arr[k][j] = value;
            value += 1;
        }
        j -= 1;
        for(int k=j;k>=i-1;k--){
            Arr[j+1][k] = value;
            value += 1;
        }
        for(int k=j;k>=i;k--){
            Arr[k][i-1] = value;
            value += 1;
        }
    }
    Arr[breakRow][breakCol] = n*n; // ręcznie uzupelnia ostatni element
    for(int i =0; i<n;i++){
        for(int j=0; j<n; j++){
            printf("%d ",Arr[i][j]);
        }
        printf("\n");
    }

}