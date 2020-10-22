# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
# różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
# dla 2315 będą to 21, 35, 231, 315.



def combinations_of_7():

    number = 2315 # przekonwertuje sobie ja na binarną wersję
    count = 0
    for i in range(2**len(str(number))+1): # 2^n kombinacji
        number_copy = number
        actual_number = 0
        for _ in range(len(str(number))+1):
            actual_number = actual_number*10 + (number_copy % 10) * (i % 2)
            number_copy //= 10
            i // 2
        if actual_number % 7 == 0:
            count +=1
    print(count)

    # na podstawie WDI i dyskretnej:
    # wiem że każdą liczbę pojedyńczą (1-9) mogę zapisać na 4 bitach 0000 - 1001
    # ilość zbiorów utworzonych z liczny jest równy 2^n, gdzie n jest równa len(number)

    # TODO:

    # zrobię pętlę wykonującą się 2^n razy, żeby zrobić wszystkie możliwe kombinacje liczb


    # druga pętla która która obskakuje po len(number)
    