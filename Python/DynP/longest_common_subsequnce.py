# Longest commmon subsequence
# LCS for input Sequences "ABCDGH" and "AEDFHR" is “ADH” of length 3.
# LCS for input Sequences "AGGTAB" and "GXTXAYB" is “GTAB” of length 4.

from collections import defaultdict


def lcs(ss1, ss2):
    LCS = defaultdict(list)

    for char1 in ss1:
        for char2 in ss2:
            if char1 is char2:
                LCS[char1] = char1
        max_lcs = len(LCS)

    return LCS


def lcs_recursive(ss1, ss2, m, n):
    if m ==0 or n == 0:
        return 0
    elif ss1[m-1] == ss2[n-1]:
        return 1 + lcs_recursive(ss1, ss2, m-1, n-1)
    else:
        return max(lcs_recursive(ss1, ss2, m-1, n), lcs_recursive(ss1, ss2, m, n-1))
    return 


seq1 = "ADB"
seq2 = "ADCGB"

# print(lcs(seq1, seq2))
print(lcs_recursive(seq1, seq2, len(seq1), len(seq2)))

