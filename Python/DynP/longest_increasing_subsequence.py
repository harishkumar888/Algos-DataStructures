# Longest increasing subsequence

# {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

my_list1 = [10, 22, 9, 33, 21, 50, 41, 60, 80] # LIS 6
my_list2 = [10, 20, 6, 8, 9, 23, 27, 25, 31, 32] # LIS 7

def get_lis_iterative(inp_list):
    LIS = [1]*len(inp_list)

    for num1 in range(len(inp_list)):
        for num2 in range(num1):
            if inp_list[num1] > inp_list[num2]:
                LIS[num1] = max(LIS[num1], LIS[num2]+1)

    maximum = 0
    for idx, num in enumerate(LIS):
        if num > maximum:
            print(inp_list[idx], end="")
            print(" ", end="")
            maximum = num

    print("")
    return maximum



def get_lis_recursive(inp_list, prev, curpos):
    if curpos == len(inp_list): return 0
    taken = 0
    if inp_list[curpos] > prev:
        taken = 1 + get_lis_recursive(inp_list, inp_list[curpos], curpos+1)
    not_taken = get_lis_recursive(inp_list, prev, curpos+1)
    return max(taken, not_taken)


def get_lis_recursive_memo(inp_list, prev, curpos, memo):
    if curpos == len(inp_list): return 0
    taken = 0

    if inp_list[curpos] > prev:
        if memo.get(curpos):
            taken = memo.get(curpos)
        else:
            taken = 1 + get_lis_recursive(inp_list, inp_list[curpos], curpos+1)

    if memo.get(curpos):
        not_taken = memo.get(curpos)
    else:
        not_taken = get_lis_recursive(inp_list, prev, curpos+1)

    max_value = max(taken, not_taken)
    memo[curpos] = max_value

    return max_value



memo = dict()
print(get_lis_recursive(my_list2, 0, 0))
print(get_lis_recursive_memo(my_list2, 0, 0, memo))
print(get_lis_iterative(my_list2))


