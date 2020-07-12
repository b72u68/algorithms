# Non-abundant sums
from math import sqrt

def isAbundant(num):
    divisors = [1]
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, num//i])
    return sum(divisors) > num

def main():
    abundant = []
    for i in range(12, 28124):
        if isAbundant(i):
            abundant.append(i)

    sumAbundant = []
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] > 28123:
                break
            sumAbundant.append(abundant[i] + abundant[j])

    notSumAbundant = []
    for i in range(1, 28124):
        if i not in sumAbundant:
            notSumAbundant.append(i)

    return sum(notSumAbundant)

if __name__ == "__main__":
    print(main())
