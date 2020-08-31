def maxSubArraySum(lst):
    best = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            currSum = 0
            for k in range(i, j):
                currSum += lst[k]
            best = max(best, sum)
    return best
