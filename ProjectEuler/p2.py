# Even Fibonacci numbers
def main():
    i1, i2 = 1, 2
    sum = 0
    while i2 <= 4000000:
        if i2 % 2 == 0:
            sum += i2
        i1, i2 = i2, i1 + i2
    return sum

if __name__ == "__main__":
    print(main())
