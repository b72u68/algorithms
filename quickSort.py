def quickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    lst = lst[1:]
    less = [x for x in lst if x < pivot]
    greater = [x for x in lst if x >= pivot]
    return quickSort(less) + [pivot] + quickSort(greater)
