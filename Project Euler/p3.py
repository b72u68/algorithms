# Largest prime number
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(int(n))
            break
    return factors

def main():
    return max(prime_factors(600851475143))

if __name__ == "__main__":
    print(main())
