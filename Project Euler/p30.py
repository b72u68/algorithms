# Digit fifth powers
def digitFifthPower(n):
    digitSum = 0
    temp = n
    while temp > 0:
        digitSum += (temp % 10) ** 5
        temp = temp // 10
    return n == digitSum

def main():
    results = []
    for i in range(10000, 99999):
        if digitFifthPower(i):
            results.append(i)
    return sum(results)

if __name__ == "__main__":
    print(main())
