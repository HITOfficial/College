# W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje do tankowania paliwa si,
# przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana przez jej odległość od punktu 0,
# tzn. si to odległość pomiędzy i-tą stacją a punktem 0. Pojazd potrafi przejechać odległość d bez potrzeby tankowania.
# Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.
# Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić wartość None.


# O(n)
def fueling_problem(F,d): # Stations Array, d -> tank size
    # 1l per 1km
    n = len(F)
    stations = 0
    d_tmp = -1
    while d < n-1:
        if d_tmp >= d: # in area [d,d+f[d]] wasn't stations
            return None
        elif F[d] != 0: # in this field is an station
            d_tmp = d
            d += F[d]
            stations += 1
        else:
            d -= 1
    return stations


d = 3
F = [0,0,5,0,0,5,0,0,0,0,0,0]
print(fueling_problem(F,d))