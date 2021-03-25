# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n,
# gdzie m jest znacznie mniejsze od n. Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.


# rozłączne


# zakładam ze zbiory składają sie z intów

# złożoność wyszukiwania: m*lon(n)
# złożoność sortowania: counta/bucket: o(n), zło



def count_sort(T): # działa mega szybko na mały range liczb
    max_el = min_el = 0
    for el in T:
        max_el = max(max_el, el) # najwiekszy element
        min_el = min(min_el, el) # najwiekszy element

    count_T = [0] * (max_el-min_el+1) # max()-min() +1 bo wlacznie z 0
    for el in T:
        count_T[el-min_el] += 1 # uwzglednienie liczb ujemnych
    for j in range(1, len(count_T)): 
        count_T[j] += count_T[j-1] # sumuje z wartoscia pod poprzednim
    sort_T = [None] * len(T) # posortowana tablica
    min_el_negation = min_el*-1
    for i in range(0,len(T)):
        sort_T[count_T[T[i] + min_el_negation]-1] = T[i] # indexy w tablicy od 0 dlatego -1
        count_T[T[i] + min_el_negation] -= 1
    for i in range(len(T)):
        T[i] = sort_T[i]

def binary_search(Arr,k,l,r):
    half = l+(r-l+1)//2
    if Arr[l] > k or Arr[r] <k or r == -1: # zeby nie wyskoczyć poza zakres
        return False
    if Arr[half] == k:
        lowest = binary_search(Arr,k,l,half-1)
        if lowest is not False:
            return lowest
        else:
            return half
    if Arr[half] > k: # idę w lewo
        return binary_search(Arr,k,l,half-1)
    else: # idę w prawo
        return binary_search(Arr,k,half+1,r)


A2 = [171,17,1,2,2,2,2,2,2,2,2,3,4,2,2,6,7,8]
A1 = [-1,5,15,9]


def subset(A1,A2): # m-> A1, n -> A2
    n = len(A2)
    count_sort(A2) # posortowane O(n)
    for el in A1:
        if binary_search(A2,el,0,n-1) is not False:
            return False
    return True


print(subset(A1,A2))