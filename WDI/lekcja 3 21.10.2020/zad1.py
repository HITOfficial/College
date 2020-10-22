# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego

# TODO:
# Input do pobrania liczby z klawiatury

value = int(input("Podaj liczbę: "))

# Funkcja do tworzenia kolejnych liczb Fibonaciego i dodawanie ich do listy

def fib_string():
    fibb_list = []
    fib1 = 1
    fib2 = 1
    for _ in range(101): # <0,100>, 
        fibb_list.append(fib2)
        (fib1, fib2) = (fib1+fib2, fib1) # klotka w ktorej pierwszy element jest suma siebie i poprzedniego
    return fibb_list

# Funkcja która porównuje liczbę pobraną od użytkownika do iloczynu dwóch  dowolnych elementów z listy fibb 

def check_if_true(user_number, fibonacci_list):
    for fib_number1 in fibonacci_list: # robię dwu wymiarową tablicę po której sobie bedę leciał
        for fib_number2 in fibonacci_list:
            if fib_number1 * fib_number2 == user_number:
                return True

print(check_if_true(value, fib_string()))