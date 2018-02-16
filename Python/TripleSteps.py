def count_ways(n, memo):
    if n<0: return 0
    if n==0: return 1
    if memo.get(n): return memo[n]
    ways = 0
    for i in [1,2,3]:
        ways += count_ways(n-i, memo)
    memo[n] = ways
    return ways
    # return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)

def count_ways_iterative(n, memo):
    table = [0]*(n+1)
    table[0] = 1
    table[1] = 1
    table[2] = 2
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n]

memo = dict()
print(count_ways(3, memo))
print(count_ways_iterative(3, memo))

