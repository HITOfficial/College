if __name__ == "__main__":
# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
    def zad1():
        a = 1
        b = 1
        print(1) # żeby dwókrotnie mieć 1
        while a < 1_000_000:
            print(a)
            tmp = a 
            a = a + b
            b = tmp

    # zad1()

# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
# Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
# sumie.
# Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n

    def zad4():
        x = int(input('wprowadź liczbę nieparzystą'))

        suma = 0
        nieparzysta = 1
        n = 0 # stopień pierwiastka

        while suma < x:
            suma += nieparzysta #sumy nieparzystych
            nieparzysta += 2 #kolejne nieparzyste
            n += 1 # kolejna nieparzysta
        
        n -= 1 # bo tworzy o 1 za dużą

        print(n)

    # zad4()

# 2
# .


# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
# Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.



# Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
# Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
# Zadanie 13. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.
# Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
# Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.
# Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.
# Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
# Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.
# Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + ...
# Zadanie 20. Dane są ciągi: An+1 =
# √
# An ∗ Bn oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do
# wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.