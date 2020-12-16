# 1. Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
# pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
# Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
# obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
# uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
# się co najmniej jeden element.

from random import randint

# zgodne piątkowo <=> w system(5), mają po tyle samo cyfr parzystych

def random_2_dimention_list(n=20):
    return [[randint(1,500) for _ in range(n)] for _ in range(n)]

def five_number(number):
    count = 0
    while number > 0:
        if (number%5)%2 == 0:
            count += 1
        number //= 10
    return count




# Na podstawie wzorca, bo przyznam że sam bym tego, w ten sposób nie wymyślił

def is_list1_part_of_list2(list1, list2):

    MAX1 = len(list1)
    MAX2 = len(list2)
    for i in range(MAX1):
        for j in range(MAX1):
            count = 0
            for k in range(MAX2):
                for l in range(MAX2):
                    if i+k < MAX1 and j+l < MAX1:
                        if five_number(list1[i+k][j+l]) == five_number(list2[k][l]):
                            count += 1 
            if count/(MAX2**2) >= 1/3:
                return True
    return False


# print(is_list1_part_of_list2(random_2_dimention_list(),random_2_dimention_list()))
# print(is_list1_part_of_list2(random_2_dimention_list(), random_2_dimention_list(15)))



def convert_system(number, system=5):
    new_system_number = 0
    power = 0

    while number > 0:
        new_system_number += (number % system) * (10** power)
        power += 1
        number //= system

    return new_system_number



def count_even(number): # zliczna liczby parzyste
    count = 0
    while number > 0:
        if (number % 10)%2 == 0:
            count += 1
        number //= 10
    return count



# Po mojemu

def find_equal_part(t1, t2): # t1 < t2
    t1_len = len(t1)
    t2_len = len(t2)
    for i in range(t2_len):
        for j in range(t2_len):
            count = 0
            for k in range(t1_len):
                for l in range(t1_len):
                    if i+k < t2_len and j+l < t2_len:
                        if count_even(convert_system(t2[i+k][j+l])) == count_even(convert_system(t1[k][j])):
                            count += 1 
            if (t2_len**2 / count) >= 1/3:
                return True


# print(find_equal_part(random_2_dimention_list(7),random_2_dimention_list(13)))



# Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
#  A: zwiększa liczbę o 3;
#  B: podwaja liczbę;
#  C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
# Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
# Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
# przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
# używanie kolejno dwóch tych samych operacji.

def A(number):
    return number + 3

def B(number):
    return number * 2

def C(number):
    tmp = number
    i = 0

    while tmp > 0:
        i += 1
        tmp //= 10

    number_as_list  = i * [0]

    while number > 0:
        i -= 1
        number_as_list[i] = number % 10
        number //= 10
    
    for i in range(len(number_as_list)): # parzyszte zwiekszam o 1 
        if number_as_list[i] %2 == 0:
            number_as_list[i] += 1

    power = -1
    val_to_increment = 0
    for el in number_as_list[::-1]:
        power += 1 
        if el >= 10:
            number += val_to_increment + el%10 * (10  ** power)
            el //= 10
            val_to_increment = el
        else:
            number += val_to_increment + el%10 * (10  ** power)
            val_to_increment = 0
    
    return number


def is_able_to_create(x,y,n,last='',combination=''):
    summary = 0
    if n >= 0:
        if x == y:
            print(combination)
            return 1
        if last != 'A':
            summary += is_able_to_create(A(x), y, n-1, 'A', combination+'A')
        if last != 'B':
            summary += is_able_to_create(B(x), y, n-1, 'B', combination+'B')
        if last != 'C':
            summary += is_able_to_create(C(x), y, n-1, 'C', combination+'C')
        
    return summary

def is_posible_to_create(x,y,n):
    return is_able_to_create(x,y,n)


print(is_posible_to_create(11,31,4))



    


