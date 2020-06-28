# Special Pythagorian triplet
def main():
    s = 1000
    for a in range(s//3):
        for b in range(a, s//2):
            c = s - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == "__main__":
    print(main())
