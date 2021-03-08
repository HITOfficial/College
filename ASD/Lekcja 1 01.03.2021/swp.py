#najwieksza suma wspólnego podciągu


t = [1,2,3,-4,-5,3,-2,-6]

def nswpN(T): # przejście liniowe
    biggest_sum = 0
    actual_biggest_sum = 0
    for i in range(len(T)):
        actual_biggest_sum += T[i]
        biggest_sum = max(actual_biggest_sum, biggest_sum)
        if actual_biggest_sum <1: # suma wspólna ujemna więc szukam kolejnego podciągu
            actual_biggest_sum = 0
    return biggest_sum

