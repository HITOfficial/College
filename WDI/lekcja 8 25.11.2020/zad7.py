# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.

# 1. zakładam że mam nieograniczoną ilość tych samych odważników, bo gdybym mógł użyć tylko po 1 odważniku to maską bym obleciał


# rozwiązanie rekurencyjne:


# przy każdej rekurencji puszczę 2:
# wrzucam dany odważnik na szalkę
# wrzucam nastepny element na szalkę
# ewntualnie gdy już będę na ostatnim elemencie z szalki, to będę go wrzucał, aż nie przeciążę, ewentualnie wyrównam odważniki w szukaną wagą

# *lista <- wypakowywuje liste

# unlimited weights 
def is_able_to_weight_unlimited(weights_list, actual_weight_index, weight_to_find, actual_weight, used_weight_list=[]): # lista odważników, aktualny odważnik, waga do odważenia, aktualana waga z odważników, dodatkowo dorzuciłem kombinację odważników odmierzających daną wagę
    if actual_weight > weight_to_find:
        return # gdy znajdę za dużą wagę to zakańczam rekurencję
    if actual_weight == weight_to_find:
        return (
            print(used_weight_list),
        )
    else:
        if actual_weight_index < len(weights_list) -1:
            is_able_to_weight_unlimited(weights_list, actual_weight_index+1, weight_to_find, actual_weight, used_weight_list) # nie daję aktualnego odważnika
            is_able_to_weight_unlimited(weights_list, actual_weight_index, weight_to_find, actual_weight + weights_list[actual_weight_index], [*used_weight_list, weights_list[actual_weight_index]]) # próbuję jeszcze raz położyć ten sam odważnik
            is_able_to_weight_unlimited(weights_list, actual_weight_index+1, weight_to_find, actual_weight + weights_list[actual_weight_index+1], [*used_weight_list, weights_list[actual_weight_index+1]]) # biorę koleny z listy odważnik jeszcze raz położyć ten sam odważnik
        if actual_weight_index == len(weights_list) -1: # gdy już nie ma kolejnych odważników lecę do wyczerpania na ostatnim
            is_able_to_weight_unlimited(weights_list, actual_weight_index, weight_to_find, actual_weight + weights_list[actual_weight_index], [*used_weight_list, weights_list[actual_weight_index]])


is_able_to_weight_unlimited(sorted([2,3,4]),-1,17,0,[])

# limit 1 of every weight
def is_able_to_weight(weight_to_find, weights_list, index_of_actual_weight=-1, actual_weight=0, used_weights_list=[]): # waga którą ma znaleźć, lista_odważników za pomocą której ma odmierzyć, aktualnie użyty odważnik, waga którą już odmierzono, użyte odważniki do obmierzenia tej wagi
    #warunki zakończenia rekurencji
    if actual_weight == weight_to_find:
        return (
            print(used_weights_list)
        )
    elif actual_weight > weight_to_find or index_of_actual_weight == len(weights_list)-1:
        return
    else:
        if index_of_actual_weight < len(weights_list) -1: # zeby nie wyskoczyć poza tablicę odważników
            is_able_to_weight(weight_to_find, weights_list, index_of_actual_weight +1, actual_weight + weights_list[index_of_actual_weight+1], [*used_weights_list, weights_list[index_of_actual_weight+1]])
            is_able_to_weight(weight_to_find, weights_list, index_of_actual_weight +1, actual_weight, used_weights_list) # nie dodaję obecnego odważnika


is_able_to_weight(13, [7,6,3,2,1,5])
