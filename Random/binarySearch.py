def binarySearch(lst, target):
    left, right = 0, len(lst)-1

    while left <= right:
        mid = (right - left)//2 + left

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
