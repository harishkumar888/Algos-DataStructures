from collections import defaultdict

# Algorithms to calculate number of ways to make change for a given amount.

# Memoized DP 
def make_change(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i-c]
    return dp[n]

# Recursive 
def count(S, m, n ):
    if (n == 0): return 1
    if (n < 0): return 0
    if (m <=0 and n >= 1): return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] )

coins = [1,2,3]
print(count(coins,3,16))
print(make_change(16))
