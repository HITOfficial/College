# Wyjeżdżacie ze znajomymi na wakacje. Macie dwa samochody i N bagaży o łącznej wadze W.
# Waga każdego z bagaży jest liczbą naturalną dodatnią. Czy jesteście w stanie tak je zapakować,
# aby w obu samochodach były bagaże o tej samej łącznej wadze?


# using knapsack problem solution
# O(n*w)

N = ["toys","glue","more toys","more more toys"]
W = [1,3,6,2]

def packing_luggage(N,W,max_w=None): # luggage and weights
    n = len(N)
    if max_w == None:
        max_w = sum(W)
    Arr = [[False]* (max_w+1) for _ in range(n)]
    # first row and col <- True    
    for row in range(n):
        Arr[row][0] = True
    for col in range(W[0]+1): # can allways make combination to recive weight equal to 0
        Arr[0][col] = True

    for row in range(1,n):
        for col in range(1,max_w+1):
            Arr[row][col] = Arr[row-1][col] # boolean
            if W[row] <= col:
                Arr[row][col] = Arr[row][col] or Arr[row-1][col-W[row]]
    
    if Arr[-1][max_w] == True and Arr[-1][max_w//2] == True:
        return True
    else:
        return False
            
print(packing_luggage(N,W))