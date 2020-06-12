def merge(lst1, lst2):
    i, j = 0, 0
    merged = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    while i < len(lst1):
        merged.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged.append(lst2[j])
        j += 1

    return merged

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    left, right = 0, len(lst)-1
    mid = (right + left)//2 - left

    return merge(mergeSort(lst[:mid]), mergeSort(lst[mid:]))
