def maxSubArraySum(lst):
    best = 0
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sum = 0 
            for j in range(i, j):
                sum += lst[k]
            best = max(best, sum)
    return best
