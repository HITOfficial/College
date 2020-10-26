# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
# jest równy 2.


def zad10(number):
    a = 2
    #a2 = 3 * 2 + 1 => 7
    # a3 = 3* 5 + 1 => 22
    # An = 3 ∗ An−1 + 1

    while number+1 > a: # bo wcześniej robie warunek dlatego number+1 bo inaczej nie znajdzie
        if number == a:
            return True
        else:
            a = 3 * a + 1
    else:
        return False


print(zad10(3))
