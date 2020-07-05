# Highly divisible triangular number
from math import sqrt

def divisors(n):
    div = []
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            if (int(n/i) == i):
                div.append(i)
            else:
                div.append(i)
                div.append(int(n/i))
    return div

def main():
    triangle_num = 0
    counter = 1
    while True:
        triangle_num += counter
        if len(divisors(triangle_num)) >= 500:
            return triangle_num
        counter += 1

if __name__ == "__main__":
    print(main())
