# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.

# 1. zakładam że mam nieograniczoną ilość tych samych odważników, bo gdybym mógł użyć tylko po 1 odważniku to maską bym obleciał


# rozwiązanie rekurencyjne:


# przy każdej rekurencji puszczę 2:
# wrzucam dany odważnik na szalkę
# wrzucam nastepny element na szalkę
# ewntualnie gdy już będę na ostatnim elemencie z szalki, to będę go wrzucał, aż nie przeciążę, ewentualnie wyrównam odważniki w szukaną wagą

# *lista <- wypakowywuje liste

def is_able_to_weight(weights_list, actual_weight_index, weight_to_find, actual_weight, used_weight_list=[]): # lista odważników, aktualny odważnik, waga do odważenia, aktualana waga z odważników, dodatkowo dorzuciłem kombinację odważników odmierzających daną wagę
    if actual_weight > weight_to_find:
        return # gdy znajdę za dużą wagę to zakańczam rekurencję
    if actual_weight == weight_to_find:
        return (
            print(used_weight_list),
            print('znaleziono wagę')
        )
    else:
        if actual_weight_index < len(weights_list) -1:
            is_able_to_weight(weights_list, actual_weight_index, weight_to_find, actual_weight + weights_list[actual_weight_index], [*used_weight_list, weights_list[actual_weight_index]]) # próbuję jeszcze raz położyć ten sam odważnik
            is_able_to_weight(weights_list, actual_weight_index+1, weight_to_find, actual_weight + weights_list[actual_weight_index+1], [*used_weight_list, weights_list[actual_weight_index+1]]) # biorę koleny z listy odważnik jeszcze raz położyć ten sam odważnik
        if actual_weight_index == len(weights_list) -1: # gdy już nie ma kolejnych odważników lecę do wyczerpania na ostatnim
            is_able_to_weight(weights_list, actual_weight_index, weight_to_find, actual_weight + weights_list[actual_weight_index], [*used_weight_list, weights_list[actual_weight_index]])


is_able_to_weight([2,3,4],0,30,0,[])



