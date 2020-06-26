# Sum square difference
def main():
    sum_square = 0
    square_sum = 0
    for i in range(1, 101):
        sum_square += i**2
        square_sum += i
    return (square_sum**2 - sum_square)

if __name__ == "__main__":
    print(main())
