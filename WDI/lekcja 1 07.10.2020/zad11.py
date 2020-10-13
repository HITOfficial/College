# if __name__ == "__main__":
#     def suma_podzielnikow_liczby(liczba):
#         suma = 0
#         i = 2
#         while i < liczba:
#             print(i)
#             if liczba % i == 0:
#                 suma += i # powiekszamy sume dzielnikow o ta liczbe
#             i += 1
#         print(suma) 

#     suma_podzielnikow_liczby(2)
#     # suma_podzielnikow_liczby(3)

# # porwnanie sumy podzielnikow liczby od 1 do n 

# # def liczby_piekne(przedzial):
# #     liczba = 2
# #     liczba_wieksza_az_do_przedzialu = liczba + 1
# #     while liczba < przedzial:
# #         while liczba_wieksza_az_do_przedzialu < przedzial:
# #             if suma_podzielnikow_liczby(liczba) == suma_podzielnikow_liczby(liczba_wieksza_az_do_przedzialu):
# #                 print(f'liczby zaprzyjaznione: {liczba} {liczba_wieksza_az_do_przedzialu}')
# #         liczba += 1



# # liczby_piekne(100)

# # 2 sposob co nie wyszedl jest ponizej

# # # liczby zaprzyjaznione: suma dzielnikow jest sobie rowna
# # # liczby zaprzyjaznione mniejsze od 1_000_000


# # # robie dwie petle jedna w drugiej i dla kazdej osobno lece 1:1_000_000
# # #                                                           2:1_000_000
# # #                                                           itd az do miliona
# # # i sprawdzam sobie po kolei sumy dzielnikow dwoch tych liczb: i jesli sa takie same to ja wypisuje


# # def podzielniki_liczby(liczba):
# #     liczba_podzielniki = []
# #     i = 1 
# #     while i < liczba:
# #         if(liczba % i == 0): # dzieli przez dwa az nie znajdzie wielokrotnosci
# #             #  print(f'dzielniki liczby: {liczba} to: {i}')
# #             liczba_podzielniki.append(i)
# #         i+=1
# #     return liczba_podzielniki


# # def suma_dzielnikow(lista):
# #     suma = 0
# #     for el in lista[0:-1]: # bez jejsamej bo jest podzielna przez sama siebie, ale musimy ja obciac w sprawdzaniu, czy jest ona liczba piekna
# #         if el != 1:
# #             suma += el
# #     return suma

# # def liczby_zaprzyjaznione(przedzial):
# #     liczba = 1
# #     while liczba <= przedzial:
# #         liczba_wieksza = liczba +1
# #         while liczba_wieksza <= przedzial:
# #             if suma_dzielnikow(podzielniki_liczby(liczba)) == suma_dzielnikow(podzielniki_liczby(liczba_wieksza)) and suma_dzielnikow(podzielniki_liczby(liczba)) > 1: # dodatkowo sprawdzam czy suma dzielnikow wieksza od 1 robie petle w petli, gdzie do pierwszej loopuje mi liczby od 1 do nieskonczonosci, a w niej druga w ktorej loopuje liczby z przedzialu od tej poprzedniej powiekszonej o 1 do konca przedzialu, wyszukujac czy znajdzie jakies liczby zaprzyjaznione
# #                 # print(f'liczby zaprzyjaznione: {liczba} {liczba_wieksza}')
# #                 pass
# #             liczba_wieksza+=1
# #         liczba+=1

# # liczby_zaprzyjaznione(300)