# Digit factorials
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def factorialDigit():
    factorialDigits = {}
    for i in range(10):
        factorialDigits[i] = factorial(i)
    return factorialDigits

def factorialDigitSum(n):
    factorialSum = 0
    factorialDigits = factorialDigit()
    while n > 0:
        factorialSum += factorialDigits[n % 10]
        n = n // 10
    return factorialSum

def main():
    results = []
    for i in range(3, 2540161):
        if i == factorialDigitSum(i):
            results.append(i)
    return sum(results)

if __name__ == "__main__":
    print(main())
