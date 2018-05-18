#              0  1  2  3  4  5  6  7
sorted_list = [1,17,19,21,27,39,41,48]

def binary_search_iterative(list, x):
    left = 0
    right = len(list)
    while(right>=left):
        mid = int((left+right)/2)
        if list[mid] < x:
            left = mid + 1
        elif list[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

def binary_search_recursive(list, x, left, right):
    while(right>=left):
        mid = int((left+right)/2)
        if list[mid] < x:
            left = mid + 1
        elif list[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1

# Incorrect and needs to be fixed.
def find_closest(list, x, left, right):
    while(right>=left):
        mid = int((left+right)/2)
        if list[mid] < x:
            left = mid + 1
        elif list[mid] > x:
            right = mid - 1
        else:
            return mid
    return min(abs(x-list[mid]), abs(x-list[mid-1]), abs(x-list[mid+1]))

# print(find_closest(sorted_list, 37, 0, len(sorted_list)))
print(binary_search_iterative(sorted_list, 39))
print(binary_search_recursive(sorted_list, 39, 0, len(sorted_list)))

