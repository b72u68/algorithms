# Smallest multiple
def gcd(x, y):
    r = max(x, y) % min(x, y)
    if r == 0:
        return min(x, y)
    return gcd(min(x, y), r)

def main():
    multiple = 1 
    for i in range(1, 21):
        div = gcd(multiple, i)
        if div == 1:
            multiple *= i
        else:
            multiple *= (i // div)
    return multiple

if __name__ == "__main__":
    print(main())
