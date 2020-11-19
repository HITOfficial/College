# Zadanie 1.
# Dana jest tablica int t[N] wypeªniona liczbami caªkowitymi. Prosz¦ napisa¢ funkcj¦, która sprawdza, czy
# mo»liwe jest "poci¦cie" tablicy na co najmniej 2 kawaªki o jednakowych sumach elementów. Do funkcji nale»y
# przekaza¢ tablic¦, funkcja powinna zwróci¢ najwi¦ksz¡ liczb¦ kawaªków, na któr¡ mo»na poci¡¢ tablic¦, lub
# warto±¢ 0, je±li takie poci¦cie nie jest mo»liwe. Na przykªad: dla tablicy [1,2,3,1,5,2,2,2,6] odpowiedzi¡
# powinno by¢ 4, bo [1,2,3|1,5|2,2,2|6].


t = [123,4,2,3,4,6,7,8,6,4,23,3,5,4,2,1]

def slice_list_on_equal_parts(list1):
    parts = 0
    for i in range(len(list1)-3):
        for j in range(i+1, len(list1)-2):
            actual_parts = 1
            sum_to_search = sum(list1[i:j+1])
            for k in range(j+1, len(list1)-1):
                flag = False
                for l in range(k+1, len(list1)):
                    if sum(list1[k:l+1]) == sum_to_search:
                        k = l
                        actual_parts +=1
                        if actual_parts >= parts:
                            parts = actual_parts
    return parts

# print(slice_list_on_equal_parts(t))


# Zadanie 2.
# Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
# ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
# równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
# par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
# maksymaln¡ liczb¦ par.


# mysle ze mozna to maską bitową obrobić
# czyli wybieramy wartość z listy 1 -> i taką samą z listy drugiej


def make_pairs(l1, l2):
    # suma ma być taka sama, czyli np biorę 3 z pierwszej -> z drugiej które tworzą taką samą sumę
    eq_pairs = 0
    for mask1 in range(1, len(l1) ** 2): # <- wszystkie kombinacje
        sum_l1 = 0
        for i1 in range(len(l1)):
            if mask1 %2 == 1:
                sum_l1 += l1[i1] 
            mask1 //= 2
            # el z drugiej
            for mask2 in range(1, len(l2) ** 2):
                sum_l2 = 0
                for i2 in range(l2):
                    if mask2 %2 == 1:
                        sum_l2 += l2[i2]
                    mask2 //= 2
                    if sum_l2 == sum_l1:
                        eq_pairs += 1
                    elif sum_l2 > sum_l1:
                        break
    return eq_pairs
    

# Zadanie 3.
# Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
# nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.


def not_unique_list(l1, l2):
    l_not_unique = list(filter(lambda x: x in l1 ,l2)) # wrzucam te, które się powtórzyły w drugiej liście
    return l_not_unique

    # za pomocą list(set(l1, l2)) mam unique wartości

x = [1,3,4,5,6,7]
y = [1,4,1001,16,6,17]

# print(not_unique_list(x,y))
