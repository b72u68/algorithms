def maxSubarraySum(lst):
    best = 0
    for i in range(len(lst)):
        sum = 0
        for j in range(i, len(lst)):
            sum += lst[j]
            best = max(sum, best)
    return best
