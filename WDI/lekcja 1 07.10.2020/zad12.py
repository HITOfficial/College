# najwiekszy wspolny dzielnik
# TODO robie sobie dzielniki liczby i przypisuje do tablicy, nastepnie sprawdzam elementy tych dwoch tablic,
# pierwsze wyszukuje najwiekszy dzielnik pierwszej liczby i sprawdzam czy taki dzielnik ma ta druga tablica,
# jesli nie ta to o jeden wczesniej z pierwszej tablicy i od nowa sprawdzam z drugiej czy jakis elementy tyle samo wynosi,
# jesli nie to analogicznie, az w ostatecznosci zawsze bedzie to 1 :D
# i sie jeblem wyzej bo zamiast tablic w pythonie sa listy

def lista_dzielnikow_liczby(liczba):
    i = 1
    lista_dzielnikow = []
    while i <= (liczba //2): # zmniejszam ilosc iteracji bo dzielniki sa do polowy liczby pazystej a w nieparzystej mniej, ile to nw pewnie okolo 1/3
        if liczba % i == 0: # jesli liczba jest podzielna to: dodaje do listy ten dzielnik
            lista_dzielnikow.append(i)
        i += 1
    lista_dzielnikow.append(liczba) # zeby skrocic liczbe iteracji recznie wpisze ta sama liczbe jako swoj dzielnik
    return lista_dzielnikow


def  najwiekszy_wspolny_dzielnik(liczba1 = 99, liczba2 = 16, liczba3 = 150):
    lista_dzielnikow_liczba1 = lista_dzielnikow_liczby(liczba1)
    lista_dzielnikow_liczba2 = lista_dzielnikow_liczby(liczba2)
    lista_dzielnikow_liczba3 = lista_dzielnikow_liczby(liczba3)
    print(lista_dzielnikow_liczba1)
    print(lista_dzielnikow_liczba2)
    print(lista_dzielnikow_liczba3)
    najwiekszy_wspolny_dzielnik = 0
    for element_z_lista1 in lista_dzielnikow_liczba1: # domyslnie jest to juz posortowane od najmniejszego dzielnika
        for element_z_lista2 in lista_dzielnikow_liczba2:
            for element_z_lista3 in lista_dzielnikow_liczba3:
                if element_z_lista1 == element_z_lista2 and element_z_lista2 == element_z_lista3: # jesli sa trzy takie same wartosci w trzech liczbach
                    if najwiekszy_wspolny_dzielnik < element_z_lista1:
                        najwiekszy_wspolny_dzielnik = element_z_lista1
    print(najwiekszy_wspolny_dzielnik)

najwiekszy_wspolny_dzielnik(120, 60, 2)