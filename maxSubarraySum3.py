def maxSubarraySum(lst):
    sum, best = 0, 0
    for i in range(len(lst)):
        sum = max(lst[i], sum+lst[i])
        best = max(best, sum)
    return best
