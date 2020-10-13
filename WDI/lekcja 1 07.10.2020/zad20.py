# Zadanie 20. Dane są ciągi: An+1 =# An ∗ Bn 
# oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do
# wspólnej granicy nazywanej średnią arytmetyczno-geometryczną.
#  Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.
from math import sqrt
import time

def ciag_a_wiekszy_o_jeden(a, b):
    a = sqrt(a * b)
    return a

def ciag_b_wiekszy_o_jeden(a, b):
    b = (a + b) / 2.0
    return b


def liczenie_ciagu(a, b):
     
    for _ in range (10): # robie 10 przejsc, przez co wynik jest w miarę dokładny
        a = ciag_a_wiekszy_o_jeden(a, b)
        b = ciag_b_wiekszy_o_jeden(a, b)

    print(a)

liczenie_ciagu(13, 76)

