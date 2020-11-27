# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.


# zakładam że mam tylko po jednym z odważników

# będą 3 warianty:
# kładę aktualny odważnik na lewo
# kładę aktualny odważnik na prawo
# pomijam aktualny odważnik


# tutaj zrobię tak: jak użyję udważnik to go będę usuwał z listy dostępnych odważników
def is_able_to_weight(weight_to_find, weights_list, actual_weight=0, used_weights_list=[], weights_to_find_added_list=[]): # waga którą ma znaleźć, lista_odważników za pomocą której ma odmierzyć, aktualnie użyty odważnik, waga którą już odmierzono, użyte odważniki do obmierzenia tej wagi
    #warunki zakończenia rekurencji
    if actual_weight == weight_to_find:
        return (
            print(used_weights_list),
            print(weights_to_find_added_list)
        )
    elif len(weights_list) == 0: # gdy już nie mam wag dostępnych
        return
    else:
        # ponieważ nie jestem pewien, czy się będą robiły referencje w listach, dlatego, dla pewności przy każdej referencji gdy modyfikuję listę, to nowa powstaje przez wypakowanie aktualnej, i dodatnie nowego elementu
        is_able_to_weight(weight_to_find + weights_list[-1], [*weights_list[:len(weights_list)-1]], actual_weight, used_weights_list, [*weights_to_find_added_list, weights_list[-1]]) # dodaję odważnik do szalki szukanej
        is_able_to_weight(weight_to_find, [*weights_list[:len(weights_list)-1]], actual_weight + weights_list[-1],[*used_weights_list, weights_list[-1]],weights_to_find_added_list) # dodaję odwaznik do szalki za pomocą której szukam
        is_able_to_weight(weight_to_find, [*weights_list[:len(weights_list)-1]], actual_weight, used_weights_list, weights_to_find_added_list) # dodaję odwaznik do szalki za pomocą której szukam

is_able_to_weight(13, [7,6,3,2,1,5])

