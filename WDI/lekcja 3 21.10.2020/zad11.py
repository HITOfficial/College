# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# jej cyfry stanowią ciąg rosnący.

# ciąg rosnący <=> an+1 > an
# będe leciał od drugiego elementu z tablicy i sprawcał czy jest wiekszy od poprzedniego, aby nie mieć kolizji z powodu braku elementu z indexem n+1 tablicy
number = int(input('type an number: '))

def zad11():
    list_of_numbers =[el for el in str(number)]
    for i in range(1,len(list_of_numbers)):
        if list_of_numbers[i-1] < list_of_numbers[i]:
            pass
        else: 
            return False
    return True

print(zad11())        