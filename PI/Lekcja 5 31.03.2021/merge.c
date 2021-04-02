#include <stdio.h>

int uniqueArray(int *Arr, int n){
    int sortedArr[n];
    int maxEl = Arr[0];
    int minEl = Arr[0];
    int uniqueArr[n];
    for(int i=0;i<n;i++){
        if(maxEl<Arr[i]){
            maxEl = Arr[i];
        }
        if(minEl>Arr[i]){
            minEl = Arr[i];
        }
        sortedArr[i] = -2147483648;
        uniqueArr[i] = -2147483648;
    }

    int countArrLen = maxEl-minEl+1; 
    int countArr[countArrLen];
    for(int i=0;i<countArrLen;i++){
        countArr[i] = 0;
    }
    for(int i=0;i<n;i++){
        countArr[Arr[i]-minEl] += 1;
    }
    for(int i=1;i<countArrLen;i++){
        countArr[i] += countArr[i-1];
    }
    for(int i=n-1;i>=0;i--){
        sortedArr[countArr[Arr[i]-minEl]-1] = Arr[i];
        countArr[Arr[i]-minEl] -= 1;
    }


    int index = 0;
    int i = 0;
    while(i < n){
        uniqueArr[index] = sortedArr[i]; // dokladam i przeskakuje przez wszystkie powtorzenia
        i+= 1;
        while(i < n && sortedArr[i] == sortedArr[i-1]){
            i += 1; // pomijam wszystkie kopie
        }
        index += 1;
    }
    for(int i=0;i<index;i++){
        printf("%d ",uniqueArr[i]);
    }
}



int main(){
    int n;
    scanf("%d",&n);
    int Arr[n*n];
    for(int i=0;i<n*n;i++){
        scanf("%d",&Arr[i]);
    }
    // linearyzacja tablicy
    uniqueArray(Arr,n*n);
}