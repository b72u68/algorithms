# Power digit sum
def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def main():
    return digitSum(2**1000)

if __name__ == "__main__":
    print(main())
