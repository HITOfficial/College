# Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory

def series_resistor(resistors):
    return sum(resistors)


def parallel_resistor(resistors):
    nominator = 1
    for i in range(resistors):
        nominator *= resistors[i]

    denominator = 0
    for i in range(len(resistors)-1):
        for j in range(i+1, len(resistors)):
            denominator += resistors[i] * resistors *resistors[j]

    return  nominator / denominator


def is_int(el):
    if el % 1 == 0:
        return True
    else:
        return False


def resistors_combination(resistors_list, i=-1, used_resistors=[]):
    if len(used_resistors) == 3:
        return(
            is_int(series_resistor(used_resistors)) or # same szeregowe
            is_int(parallel_resistor(used_resistors)) or # same równoległe
            is_int(parallel_resistor(series_resistor(used_resistors[0]) + parallel_resistor([*used_resistors[1:]]))) or # szeregowy jako pierwszy
            is_int(parallel_resistor(series_resistor(used_resistors[1]) + parallel_resistor([*used_resistors[0], *used_resistors[2]]))) or # szeregowy jako drugi
            is_int(parallel_resistor(series_resistor(used_resistors[2]) + parallel_resistor([*used_resistors[0], *used_resistors[2]]))) # szeregowy jako trzeci
            
        )
    if len(used_resistors) < 3 and i < len(resistors_list)-1: # dokładamy rezystory 
        return (
            resistors_combination(resistors_list, i+1, [*used_resistors, resistors_list[i+1]]) or # dodajemy aktualny rezystor
            resistors_combination(resistors_list, i+1, [*used_resistors]) # nie dokładamy aktualny rezystor
        )
    return False

t = [1,2,3,4,5,3,2,1]

print(resistors_combination(t))