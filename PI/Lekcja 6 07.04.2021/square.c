#include <stdio.h>

int main(void){
    int n,area;
    scanf("%d %d",&n,&area);
    int Arr[n][n];
    for(int i=0;i<n;i++){ // nadpisuje tablice
        for(int j=0;j<n;j++){
           scanf("%d",&Arr[i][j]); 
        }
    }

    int A[n*n][2]; // w ten tablicy bede zapisywal kordy znalezione kwadraty
    int index = 0;
    for(int i=0; i<n;i++){
        for(int j=0;j<n;j++){
            int flag = 0; // zeby pare razy nie wypisywac ten sam srodek, roznych kwadratow
            for(int k=1;k<n;k++){
                if(i-k < 0 || i+k >= n || j-k < 0 || j+k >= n){ // wyskoczy poza tablice
                    break;
                }

                int elements = 1;
                int sum_K = 0;
                for(int row=i-k;row<=i+k;row++){ // tworze kwadraty
                    for (int col=j-k;col <= j+k; col++){
                        if(row != i || col != j){ // pomijam srodek kwadratu
                            sum_K += Arr[row][col];
                            elements += 1;
                        }
                    }
                }
                if(elements %2 == 1 && sum_K == area){
                    if(flag == 0){ // pierwszy kwadrat o takim srodku
                        A[index][0] = i;
                        A[index][1] = j;
                        index += 1;
                    }
                    flag = 0;
                }
            }
        }
    }
    printf("%d\n",index);
    for(int i=0;i<index;i++){
        printf("%d %d\n", A[i][0],A[i][1]);
    }


}