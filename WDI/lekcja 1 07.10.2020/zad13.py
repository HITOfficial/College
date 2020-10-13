def lista_dzielnikow_liczby(liczba):
    i = 1
    lista_dzielnikow = []
    while i <= (liczba //2): 
        if liczba % i == 0:
            lista_dzielnikow.append(i)
        i += 1
    lista_dzielnikow.append(liczba)
    return lista_dzielnikow

def iloczyn_wyrazow_tab(NWW, lista_dzielnikow_liczba1):
    for el in lista_dzielnikow_liczba1:
            NWW *= el
    return NWW

def  najmniejszy_wspolny_dzielnik(liczba1 = 99, liczba2 = 16, liczba3 = 150):
    lista_dzielnikow_liczba1 = lista_dzielnikow_liczby(liczba1)
    lista_dzielnikow_liczba2 = lista_dzielnikow_liczby(liczba2)
    lista_dzielnikow_liczba3 = lista_dzielnikow_liczby(liczba3)

    # print(lista_dzielnikow_liczba1)
    # print(lista_dzielnikow_liczba2)
    # print(lista_dzielnikow_liczba3)

    wspolne_dzielniki = []
    NWW = 1
    
    for element_z_lista1 in lista_dzielnikow_liczba1:
        for element_z_lista2 in lista_dzielnikow_liczba2:
            for element_z_lista3 in lista_dzielnikow_liczba3:
                if element_z_lista1 == element_z_lista2 and element_z_lista2 == element_z_lista3:
                    wspolne_dzielniki.append(element_z_lista3)
                    lista_dzielnikow_liczba1.remove(element_z_lista1)
                    lista_dzielnikow_liczba2.remove(element_z_lista2)
                    lista_dzielnikow_liczba3.remove(element_z_lista3)

    NWW = iloczyn_wyrazow_tab(NWW, lista_dzielnikow_liczba1)
    NWW = iloczyn_wyrazow_tab(NWW, lista_dzielnikow_liczba2)
    NWW = iloczyn_wyrazow_tab(NWW, lista_dzielnikow_liczba3)

    print(NWW)
    
najmniejszy_wspolny_dzielnik(12, 6, 4)