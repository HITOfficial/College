// Mamy dany zestaw n odważników o masach danych liczbami naturalnymi. Napisz program, który sprawdza,
// czy zadany ciężar w można zważyć przy pomocy wagi dwuszalkowej (czyli odważniki mogą być po obu stronach wagi).
#include <stdio.h>




// uwzgledniam tylko położenie na 1 lub 2 szalke, bez pomijania ciezarka, bo wtedy nie przejdzie testów
int weightPan(int *T, int n, int w, int c, int id){ // Table, T length, searching weight, currently weight, actual index of weight
    if(w == c){
        return 1;
    }
    if(c > w || n == id){ // wartosc za duza albo przeskoczymy za daleko
        return 0;
    }
    int ret_val = ( 0
    || weightPan(T,n,w,c+T[id],id++)
    || weightPan(T,n,w+T[id],c,id++));

    return ret_val;
}


int main(void){
    int n, m; // ilość odważników, masa
    scanf("%d %d", &n, &m);
    int T[n];
    int w_sum = 0; 
    for(int i=0; i<n; i++){ // zapełnienie wartosciami odważników
        scanf("%d", &T[i]);
        w_sum += T[i];
    }
    if(w_sum < m){
        printf("NO"); // sprawdza czy odwazniki nie sa mniejsze niz waga szukana, bo inaczej nie przejdzie testow
    }
    else if(weightPan(T,n,m,0,0) == 1){
        printf("YES");
    }
    else{
        printf("NO");
    }
}