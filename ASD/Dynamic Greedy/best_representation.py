# We have the given strings (words) S = [s1, sn] and the string t string. It is known that t for a given possibility as a combination of the name
# of a certain number of strings with S (with repetitions). For example, for S = [s1, s2, s3, s4, s5] where s1 = ab, s2 = abab, s3 = ba and s4 = bab,
# s5 = b, the string = ababbab could be known, among others, as s2s4 or as s1s1s3s5.
# Such a choice. By the length Ist Ist the shortest Si by the length to L - for s2s4 the width is up to 3, and for s1s1s3s5 the width is up to 1.
# Implement an algorithm to go to input S and t will find the transition to the first input. Estimate the runtime of the algorithm.

# complexity:
# - time O(N*M), where N length of t string, M, length of longest string from S array
# - space O(T)


def best_representation(S, t):
    t_len = len(t)
    answer = [-1]*t_len
    for i in range(t_len+1):
        for s in S:
            if i+1 >= len(s):
                word = t[i-len(s)+1:i+1]
                if word == s:
                    # longest part is an answer
                    answer[i] = max(max(len(s), answer[i -
                                                       len(s)]), answer[i])
    return answer[-1]


S = ["ab", "abab", "ba", "bab", "b"]
t = "ababbab"

print(best_representation(S, t))
