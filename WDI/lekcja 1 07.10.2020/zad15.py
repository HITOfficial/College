from math import sqrt
import time

def lista_z_dzielnikami():
    lista_elementow_do_wzoru = []
    i = 0
    while i < 1000: # bo inaczej zrobie infinity loop'a
        x = sqrt(0.5) # wrzuce to w liste i lacznikiem wszystkich elementow bedzie *
        if i == 0:
            lista_elementow_do_wzoru.append(x)
        else:
            lista_elementow_do_wzoru.append(sqrt(0.5 + 0.5 * lista_elementow_do_wzoru[-1])) # wykoryzstalem tylko jedna zmiennna x ktora sobie przemnazam przez 0.5 jak we wzrorze
        i += 1

    return lista_elementow_do_wzoru # zwroce sobie tylko liste tych el
 
def laczy_liste_w_jeden_element(lista):
    liczba_pi = 1 # bo mnazac przez 0 bedzie lipa a takto 1 nie modyfikuje wgl zawartosci
    for el in lista:
        liczba_pi *= el
    return liczba_pi 

def liczba_pi():
    liczba_pi = laczy_liste_w_jeden_element(lista_z_dzielnikami()) / 2
    print(f'liczba pi jest rowna: {liczba_pi}')

liczba_pi()

# lista = [1,23,4,5,6,7,8]
# newList = lista[-1::]
# print(newList)
