# Merge Sort

def merge_sort(lis):
    if len(lis) == 1 or len(lis) == 0:
        return lis
    else:
        mid = len(lis)//2
        a = merge_sort(lis[:mid])
        b = merge_sort(lis[mid:])
        lis = merge(a, b)
        return lis

def merge(l, r):
    if not l: return r
    if not r: return l
    res = []
    i = 0
    j = 0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    if i<len(l):
        res.extend(l[i:])
    if j<len(r):
        res.extend(r[j:])
    return res

unsorted_list = [83,2,5,7,9,12,65,1,33,20]
print(merge_sort(unsorted_list))

