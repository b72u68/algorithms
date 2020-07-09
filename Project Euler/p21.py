# Amicable number
from math import sqrt

def divisors(n):
    div = [1]
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            if n // i == i:
                div.append(i)
            else:
                div.extend([i, n//i])
    return div

def isAmicable(n):
    divSum = sum(divisors(n))
    if sum(divisors(divSum)) == n:
        return True
    return False

def main():
    sum = 0
    for i in range(10000):
        if isAmicable(i):
            sum += i
    return sum

if __name__ == "__main__":
    print(main())
