# 10001st prime
import math

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def main():
    counter = 0
    num = 2
    while counter < 10001:
        if check_prime(num):
            counter += 1
        num += 1
    return num - 1

if __name__ == "__main__":
    print(main())
