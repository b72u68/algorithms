def maxSubarraySum(lst):
    best = 0
    for i in range(len(lst)):
        currSum = 0
        for j in range(i, len(lst)):
            currSum += lst[j]
            best = max(sum, best)
    return best
