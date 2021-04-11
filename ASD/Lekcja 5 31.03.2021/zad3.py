from random import randint

# O(n*MaxWeight)
def get_solution(Arr,W,P,i,w):
    if i <0: return [] # uwzglednione wszystkie przedmioty
    if i == 0:
        if W[0] <= w: # jeszcze podany przedmiot nie przekracza wagi
            return [0]
        return []
    if w >= W[i] and P[i]+Arr[i][w-W[i]] >= Arr[i][w]: # lepiej zabrac aktualny przedmiot
        return get_solution(Arr,W,P,i-1,w-W[i])+[i]
    return get_solution(Arr,W,P,i-1,w)


def knap_sack(W,P,max_W): # wagi, punkty(cena)
    n= len(W)
    Arr = [[0]*(max_W+1) for _ in range(n)]
    for i in range(W[0],max_W+1): # żeby uwzględnić pierwszy przedmiot, a gdyby był za ciężki niż dopuszczalna waga, to ominie tą pętle
        Arr[0][i] = P[0]
    for i in range(1,n):
        for w in range(1,max_W+1):
            Arr[i][w] = Arr[i-1][w] # ustawiam defaultowo poprzednika
            if w >=W[i]: # waga pod aktualnym przedmiotem jest mniejsza niz aktualnie rozwazana waga
                Arr[i][w] = max(Arr[i][w],P[i]+Arr[i-1][w-W[i]]) # poprzednik, wartość aktualnego + z poprzednika: maxymalna wartość do pozostałego udźwigu
    Indexes = get_solution(Arr,W,P,n-1,max_W)
    return Arr[n-1][max_W-1], [P[Indexes[i]] for i in range(len(Indexes))]



W = [randint(1,300) for _ in range(110)]
P = [randint(1,300) for _ in range(110)]
max_W = 10000
print(knap_sack(W,P,max_W))
