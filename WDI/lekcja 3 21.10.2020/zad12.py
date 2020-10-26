# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta zawiera cyfrę równą liczbie swoich cyfr.
number_from_keyboard = int(input('enter a number'))

def zad12_idea1(number):
    for single_number in str(number): 
        print(len(str(number)), single_number, sep = '  ')
        if int(single_number) == len(str(number)):
            return True

print(zad12_idea1(number_from_keyboard))

# PO SZKOLNEMU
def zad12_idea2(number):
    tmp_number = number
    count_number = 0
    while tmp_number > 0:
        count_number += 1
        tmp_number //= 10
    
    while number > 0:
        if number % 10 == count_number: # sprawdzam ostatnią cyfrę z liczby czy jest równa ilości liczb 
            return True
        number //= 10
    else: 
        return False

print(zad12_idea2(number_from_keyboard))