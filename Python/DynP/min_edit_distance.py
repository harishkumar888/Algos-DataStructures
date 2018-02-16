'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.
'''

def edit_distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    return 1+min(
        edit_distance(str1, str2, m-1, n-1),
        edit_distance(str1, str2, m-1, n),
        edit_distance(str1, str2, m, n-1)
    )

def edit_distance_iterative(str1, str2, m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j ==0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min (dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[m][n]

day1 = "azcedf"
day2 = "abcdef"

memo = [[0 for x in range(len(day1))] for y in range(len(day2))]
# print(edit_distance(day1, day2, len(day1), len(day2)))
print(edit_distance_iterative(day1, day2, len(day1), len(day2)))

