# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

# jak najmniej elementów w squadzie
# zrobiłem to maską bitową
# tzn łapę elementy, sumuję wartości pod nimi, i przyrównuję z indexami pod którymi stoją


def smallest_val_equal_index(list_of_values):
    smallest = False
    for mask_bit in range(1,2**len(list_of_values)): # 001 zaczynam od przynajmniej 1 elementu
        sum_of_el = 0
        sum_of_id = 0
        # będę dodawał wszystkie elementy z listy, zgadzające się z maską i na końcu sprawdzał, czy zgadza się wartość id z sumą wartości
        for i in range(len(list_of_values)-1, 0, -1): # idę od ostatniego elementu z listy, bo tak ustawiłem maskę -> 0001, 0010... itd
            if mask_bit %2:
                sum_of_id += i
                sum_of_el += list_of_values[i] 
            mask_bit //= 2
        
        if sum_of_el == sum_of_id and (smallest == False or smallest > sum_of_id):
            smallest = sum_of_id # gdy nic nie wsadziłem w smallest, to będzie to pierwsza kombinacja spełniająca polecenie, albo kolejne juz kombinacja, której wartość jest mniejsza, niż dotychczasowa

    return smallest

print(smallest_val_equal_index([1,2,3,3,2,6,34,2,34,12,3,6,7]))
