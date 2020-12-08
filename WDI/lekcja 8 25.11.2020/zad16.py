# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład 00ula00 → 117, 108, 97
# oraz 00exe00 → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
# znaleziony wyraz.

def world_to_asci_sum(n): # konewertuje wszystkie elementy na asci
    asci_list = list(map(lambda x: ord(x), n))
    return sum(asci_list)


def sum_vowels(w):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len(list(filter(lambda x: x in vowels, w)))


def subset(word1, word2, s2=0, e2=1):
    m = word2[s2:e2]
    flag = False
    if s2 < e2 and s2 >=0 and e2 <= len(word2):
        if world_to_asci_sum(word1) == world_to_asci_sum(word2[s2:e2]) and sum_vowels(word1) == sum_vowels(word2[s2:e2]):
            print(word2[s2:e2])
            return True

        return (
            flag or
            subset(word1, word2, s2, e2+1) or
            subset(word1, word2, s2+1, e2)
            )
    return False

    


def word(s1,s2):
    return subset(s1, s2)

print(word('00ula00', '00exe00'))


