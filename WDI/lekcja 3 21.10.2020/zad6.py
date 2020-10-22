# Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.

number = 120

def dividing_list(number):
    dividing_list = []
    i = 1
    while i <= number // 2: # szukamy tylko dzielników do połowy tej liczby
        if number %i == 0:
            dividing_list.append(i)
        i+=1
    return dividing_list # tworze listę z wszystkimi dzielnikami tej liczby


def lowest_difference(dividing_list, number):
    lowest_difference = number # pobrałem liczbę z której będę liczył wartość pod modułem z dzielników tak, aby się móc na czymś wzorować i mieć do warunku
    number1, number2 = 0, 0 # zrobiłem dwie zmienne na początku, do których potem będę przypisywał liczby spełniające warunek
    for el1 in dividing_list:
        for el2 in dividing_list:
            if abs(el1 - el2) < lowest_difference and el1 != el2 and el1 * el2 == number: # w tym warunku wstępnie najmniejszą różnicą jest liczba początkowa z której sprawdzamy dzielniki, następnie robię 2 wymiarową tablicę i iteruję sobie po wszystkich elementach, sprawdzając, czy wartość bezwzględna tych dwóch elementów jest mniejsza od liczby z początku, następnie, czy są to dwie różne liczby, oraz, czy iloczyn tych dwóch liczb jest równy liczbie z której mamy dzielniki
                lowest_difference = abs(el1 - el2) # gdy wejdziemy do warunku, to do najmniejszej róznicy przypisujemy wartość bezwzględną tych 2 elementów
                number1 = el1 # do tych dwóch liczb, z lini 18 przypisuję wartośći spełniające warunek
                number2 = el2
    return (number1, number2) # zwracam dwie najmniejsze liczby spełniające ten warunek


print(f'najmniejsza róznica dzielnych wynosi: {lowest_difference(dividing_list(number), number)}')
# print(dividing_list(120))

