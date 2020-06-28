from math import sqrt

# using check primes algorithm
def check_primes(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# using Sieve of Eratosthenes algorithm
def getPrimes(limit):
    numList = [x for x in range(2, limit+1)]
    primeIdx = 0
    while primeIdx < len(numList):
        if numList[primeIdx] != 0:
            multipleIdx = primeIdx + numList[primeIdx]
            while multipleIdx < len(numList):
                numList[multipleIdx] = 0
                multipleIdx += numList[primeIdx]
        primeIdx += 1
    return numList

def main():
    primeList = getPrimes(2*(10**6))
    return sum(primeList)

if __name__ == "__main__":
    print(main())
