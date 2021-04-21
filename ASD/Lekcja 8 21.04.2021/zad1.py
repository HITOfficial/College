from random import randint
# Arr = [randint(1,10) for _ in range(10)]

Arr = [1,2,4,3,2,11,6]
def black_forest(Arr):
    n = len(Arr)
    if n == 0:
        return 0
    if n == 1:
        return 0
    tree_sum = [0] * n
    tree_sum[-1] = Arr[-1] # to do start alghoritm i need to mark up 2 last trees
    if Arr[-1] > Arr[-2]: # better value using last tree then  before the last one
        tree_sum[-2] = Arr[-1]
    else:
        tree_sum[-2] = Arr[-2]
    for i in range(n-3,-1,-1):
        prev = tree_sum[i+1]
        actual = tree_sum[i+2] + Arr[i]
        if actual > prev:
            tree_sum[i] = actual
        else:
            tree_sum[i] = prev
            
    return tree_sum[0]

print(black_forest(Arr))