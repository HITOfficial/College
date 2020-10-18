# 3 -> 10
# 4 -> 500
# 5 -> 3000
# 6 -> 17_000_000

def ile_kasy(ile_liczb, domyslnie):
    if ile_liczb == 3:
        return 10
    elif ile_liczb == 4:
        return 500 
    elif ile_liczb == 5:
        return 3000
    elif ile_liczb == 6:
        return 17_000_000 
    return domyslnie

f = {
    3: 10,
    4: 500,
    5: 3000,
    6: 17_000_000,
}

y = f[x]
