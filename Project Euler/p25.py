# 1000-digit Fibonacci number
def fibonacci(n):
    f1, f2 = 1, 1
    for _ in range(n-2):
        f1, f2 = f2, f1 + f2
    return f2

def main():
    n = 3
    while True:
        fn = fibonacci(n)
        if len(str(fn)) >= 4:
            return n
        n = n + 1

if __name__ == "__main__":
    print(main())
