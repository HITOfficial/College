# Zadanie 6. Proszę napisać program rozwiązujący równanie x
# x = 2020 metodą bisekcji.

def number_to_pow():
    a = 0 # podaje przedzial w ktorym ma szukać
    b = 100
    m = (a + b) / 2 # to jest dzielenie na połowę metodą bisekcji
    epsilon = 0.001
    while(m ** m - 2020) > epsilon: # gdy zmienna podniesiona do samej siebie miedzy 2020 bedzie sie roznila mniej niz epsilon to petla sie przerwie 
        if (m ** m) > 2020: # 50^50 <- wieksze
            b = m
            m = (a + b) / 2
        if (m ** m) < 2020:
            a = m
            m = (a + b) / 2
    print(m)
            
            
number_to_pow()




# tak ma robić:
# przyjmuje 2020 jako argument
#    - liczy 