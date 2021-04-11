# knapsack problem O(n*sum(Profits))
from random import randint
from math import inf

W = [randint(1,100) for _ in range(50)]
P = [randint(1,100) for _ in range(50)]


def get_path(Arr,W,P,p,i): # Arrays: 2Dim, Weights, Profits, profit remaing, index, last price
    if i <0 or p == 0: return [] # uwzglednione wszystkie przedmioty
    if i > 0 and  Arr[i][p] < Arr[i-1][p]:
        return get_path(Arr,W,P,p-P[i],i-1)+[P[i]] # uwzgledniam aktualnie rozpatrzany profit
    return get_path(Arr,W,P,p,i-1)


def knapsack_by_profits(W,P,max_W):
    n = len(W)
    P_sum  = sum(P)
    Arr = [[inf for _ in range(P_sum+1)] for _ in range(n)]
    for i in range(P[0]+1): # uzupełniam możliwosci przy uzyciu tylko pierwszego elementu
        Arr[0][i] = W[0]
    for i in range(n): # markuje pola wagami defaultowymi pod danymi indexami
        Arr[i][P[i]] = W[i]

    for i in range(1,n):
        for j in range(P_sum,-1,-1):
            if j < P_sum: # ponieważ zaczynam od końca, uwzględniam dodatkowo kolejny index
                Arr[i][j] = min(Arr[i-1][j],W[i] + Arr[i-1][j-P[i]],Arr[i][j],Arr[i][j+1])
            else:
                Arr[i][j] = min(Arr[i-1][j],W[i] + Arr[i-1][j-P[i]],Arr[i][j])
    for j in range(P_sum,-1,-1):
        if Arr[n-1][j] <= max_W:
            return get_path(Arr,W,P,j,n-1)


print(knapsack_by_profits(W,P,50))
