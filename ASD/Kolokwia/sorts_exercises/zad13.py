# sprawdź czy podane słowa są anagramami (UNICODE)

a = "dsadaj312kfdf&*$(@#&@KsD"
b = "@adaj213kfddf&*$(@#&KFDs"
def is_anagram(a,b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    Arr = [0] *(2**16)
    for letter in a:
        Arr[ord(letter)] += 1    
    for letter in b:
        Arr[ord(letter)] -= 1
    for el in Arr:
        if el != 0:
            return False
    return True


print(is_anagram(a,b))

