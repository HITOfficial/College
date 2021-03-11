# Proszę zaimplementowad funkcje:
# double AverageScore(double A[]int n, int lowest, int highest);
# Funkcja ta przyjmuje na wejściu tablice h liczby rzeczywistych (ich rozklad nie jest
# znany, ale wszystkie są parami różne i zwraca srednią wartość podanych liczb po
# odrzuceniu lowest najmniejszych oraz highest największych. Zaimplementowana
# funkcja powinna byd możliwie jak najszybsza. Proszę oszacowadliej złożoność
# czasowa
# (oraz bardzo krótko uzasadnic to oszacowanie)


# wybuduje kopiec na wszystkie elementy:
# przesortuje max_cheap highest, następnie przebuduje kopiec malejaco, i min_cheap na lowest elementów
# po tym przelece i zsumuje pozostałe elementy

def max_cheap(T,n,i):
    left = 2*i+1
    right = 2*i+2
    i_copy = i
    if left < n and T[left] > T[i_copy]:
        i_copy = left
    if right < n and T[right] > T[i_copy]:
        i_copy = right
    if i_copy != i:
        T[i_copy], T[i] = T[i], T[i_copy]
        max_cheap(T,n, i_copy)


def min_cheap(T,n,i):
    left = 2*i+1
    right = 2*i+2
    i_copy = i
    if left < n and T[left] < T[i_copy]:
        i_copy = left
    if right < n and T[right] < T[i_copy]:
        i_copy = right
    if i_copy != i:
        T[i_copy], T[i] = T[i], T[i_copy]
        min_cheap(T,n, i_copy)


def build_cheap_desc(T,n):
    for i in range((n-1)//2,-1,-1):
        max_cheap(T,n,i)


def build_cheap_asc(T,n):
    for i in range((n-1)//2,-1,-1):
        min_cheap(T,n,i)


def average_score(T, lowest, highest):
    n = len(T)    
    build_cheap_desc(T,n) # buduje kopiec rosnący
    # sortuje highest najwiekszych elementow
    for i in range(n-1,n-highest-1,-1):
        T[i],T[0] = T[0],T[i]
        max_cheap(T,i,0)
    n = n-highest # ostatnich highest indexów są najwiekszymi z tablicy
    build_cheap_asc(T,n) # buduję kopiec malejącu
    for i in range(n-1,n-lowest-1,-1):
        T[i],T[0] = T[0],T[i]
        min_cheap(T,i,0)
    el_sum = 0
    for i in range(n-lowest):
        el_sum += T[i]
    average = el_sum / (n-lowest)
    return average

#           złożoność:
# elementy rosnące: n + highest*log(n)
# elementy malejące: n-h + last*log(n-highest)
# zsumowanie pozostałch: n-highest-lowest