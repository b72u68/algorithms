# Name scores
from string import ascii_uppercase

def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

def main():
    with open('names.txt') as f:
        names = f.read().split(',')
        names.sort()
    return sum(i*score(name) for i, name in enumerate(names, 1))

if __name__ == "__main__":
    print(main())
