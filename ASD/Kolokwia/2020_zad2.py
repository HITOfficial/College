# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga 
# czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

def nuber_as_as_sum_others(T):
    # algo n^3 w najgroszym przypadku
    for i in range(len(T)):
        is_a_sum_of_others = False # zakładam, początkowo, że nie jest
        for j in range(len(T)):
            if j == i:
                continue
            for k in range(len(T)):
                if k == j or k == i:
                    continue # warunek żeby nie brać dwa razy tej samej liczby
                if T[i] == T[j]+T[k]:
                    is_a_sum_of_others = True
                    break
            if is_a_sum_of_others:
                break
        if is_a_sum_of_others == False:
            return False
    return True

