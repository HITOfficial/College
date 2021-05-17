# Złodziej włamuje się do sklepu z przedmiotami o wagach i cenach, będących liczbami naturalnymi dodatnimi.
# Chowa je do plecaka, w którym może unieść rzeczy o łącznej maksymalnej wadze Wmax.
# Tak, tak, znamy tę historię. Ale tym razem złodziejowi nie zależy na tym, by ukraść artykuły o najwyższej możliwej łącznej cenie.
# Interesuje go za to, na ile sposobów może wybrać przedmioty, aby ich łączna cena była równa co najmniej Cmin oraz aby ich łączna waga nie przekraczała Wmax.

# >= CMIN <= WMAX

#O(N*C_sum*W_max)

C = [1,2,5,2]
W = [3,4,7,2]


def knasack_combinations(C,W,C_min,W_max): # Costs, Weights, minimum cost, maximum weight
    n = len(C)
    C_sum = sum(C)
    W_max = sum(W)

    Arr = [[[0]*(W_max+1) for _ in range(C_sum+1)] for _ in range(n)] # knapsack array N^3

    # Filling combination using first item only
    for cost in range(C[0],C_sum+1):
        for weight in range(W[0],W_max):
            Arr[0][cost][weight] = 1 # first combination to recive 

    for index in range(1,n):
        for cost in range(C_sum+1):
            for weight in range(W_max+1):
                Arr[index][cost][weight] = Arr[index-1][cost][weight]
                if W[index] <= W_max and C[index] >=0: # can take this item
                    Arr[index][cost][weight] = max(Arr[index][cost][weight],1 + Arr[index][cost-C[index]][weight-W[index]])
    maximum = 0
    tmp_tpl = (0,0)
    for cost in range(C_min,C_sum+1):
        for weight in range(W_max+1):
            maximum_tmp = maximum
            maximum = max(maximum,Arr[-1][cost][weight])
            if maximum_tmp != maximum:
                tmp_tpl = (cost,weight)
    return  maximum, tmp_tpl

print(knasack_combinations(C,W,1,11))
    