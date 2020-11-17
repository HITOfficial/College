# Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
# licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie

# dodawanie liczb wymiernych


def NWD(m1, m2): # najwiekszy wspólny dzielnik, bo przyda się do wyznaczenia najmniejszesz wspólnej wielokrotności
    #algorytmem Euklidesa
    while m1 != m2:
        if m1 > m2:
            m1 -= m2
        else:
            m2 -= m1
    return m1

def NWW(m1, m2):
    return int(((m1 *m2) // NWD(m1, m2)))


def operation_on_irration_number(number1, sign, number2 = (1,1)): # potęgowania i pierwiastkowania nie robiłem bo delikatnie musiał bym zmienić wnętrze
    l1 = number1[0] # tuple są imutable
    m1 = number1[1]
    l2 = number2[0]
    m2 = number2[1]

    if sign == '+'  or sign == '-':
        common_denominator = NWW(m1,m2)
        l1 *= int(common_denominator // m1) # sprowadzam do wspólnego mianownika liczby
        l2 *= int(common_denominator // m2)

        if sign == '+':
            return (l1+l2, common_denominator)
        if sign == '-':
            return (l1-l2, common_denominator)
    
    if sign == '/' or sign == '*':
        nominator = 0 # najpierw musze zadeklarować jakoś zmienne, żeby w warunkach je nadpisać
        denominator = 0

        if sign == '*':
            nominator = int(l1 * l2)
            denominator = int(m1 * m2)    
        if sign == '/':
            nominator = int(l1 * m2)
            denominator = int(l2 * m1) # nie sprawdzałem ale dla pewności, konwetuje na inta wszystkie wyrażenia

        nominator, denominator = int(nominator // NWD(nominator, denominator)), int(denominator // NWD(nominator, denominator)) # żeby nie używać dodatkowych zmiennych tuplem skracam o ile mogę licznik i mianownik, przez najwiekszy wspólny dzielnik
        return (nominator, denominator)    


print(operation_on_irration_number((3,8),(1,2),'/'))
