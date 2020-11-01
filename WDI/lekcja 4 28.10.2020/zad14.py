# Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
# grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
# wartości prawdopodobieństwa dla N z zakresu 20-40.


def zad14():
    days_in_year = 366 # dni w roku przestępny
    part_of_probability = 1 # jedynke sobie juz deklaruje bo potem będę ją modyfikował, oraz w założeniu wzoru do tego ciagu n >= 2
    for n in range(2, 41): # <2,40> przedział
        part_of_probability *= (days_in_year- n + 1) / days_in_year # bo jak we wzorze mam lecieć do n-1 elementów w sumie

        if n >= 20 and n <= 40:
            print(f'n:{n} -> {round((1 - part_of_probability), 4)}')


    # wzór ogólny:
    # (366- n) / 366



zad14()