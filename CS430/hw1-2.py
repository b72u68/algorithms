import sys

def main(array):
    left = 0
    right = len(array) - 1
    mid = 0

    while left < right:
        mid = (left + right) // 2
        if array[mid] < array[mid +1]:
            left = mid + 1
        elif array[mid] > array[mid+1]:
            if array[mid] < array[mid-1]:
                right = mid - 1
            else:
                return array[mid]

    return max(array[left], array[right])

if __name__ == "__main__":
    print(main([120, 100, 80, 20, 0]))
