# Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
# wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

# Nw dokładnie o co chodzi ale na oko to:
# obskoczyć tego numbera i pousuwać wszystkie ostatnie zera


# ZADANIE DO POPRAWKI BO NW O CO CHODZI
def zad5(number):
    number_tmp = number
    # 10^ wartość czyli => pozostałych elementów  ??
    while number_tmp % 10 == 0:
        number_tmp //=10 # <= usunąłem ciąg ostatnich zer z liczby

    return 10**number_tmp # <= zwróci i tak inta 64 bitowego wiec pasuje potem przemienic na "string" chyba

print(zad5(352000))
    