from random import randint
# podobnie jak w knapsack problemie
# O(n*k)
def subsequence_sum(A,k):
    n = len(A)
    Arr =[[False for _ in range(k+1)] for _ in range(n)]
    for i in range(1,n): # szukany podciag dajacy 0 zawsze mozliwy do stworzenia
        Arr[i][0] = True
    if A[0] <= k: # uwzględniam pierwszy element
        Arr[0][A[0]] = True
        
    for i in range(1,n):
        for j in range(1,k+1):
            Arr[i][j] = Arr[i-1][j]
            if A[i] <= j:
                Arr[i][j] = Arr[i][j] or Arr[i-1][j-A[i]]
    return Arr[n-1][k]



A = [randint(1,6) for _ in range(6)]
print(subsequence_sum(A,15))