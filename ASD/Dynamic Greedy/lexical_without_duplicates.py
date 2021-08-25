# complexity:
# - time O(N)
# - space O(1) string without duplicates / O(26) array to mark up used letters


def lexical_without_duplicates(S):
    # low letters only
    used = [False]*26
    without_duplicates = ""
    for l in S:
        idx = ord(l)-97
        if used[idx] is False:
            used[idx] = True
            without_duplicates += l
    return without_duplicates


print(lexical_without_duplicates("wwwwawwwwa"))
print(lexical_without_duplicates("dsafgfsfadfassfdsaffdssf"))
