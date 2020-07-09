# Factorial digit sum
def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    return digitSum(factorial(100))

if __name__ == "__main__":
    print(main())
