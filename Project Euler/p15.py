# Lattice paths
def countPath(gridSize):
    paths = 1
    for i in range(gridSize):
        paths *= (2 * gridSize) - i
        paths /= i + 1
    return int(paths)

def main():
    return countPath(20)

if __name__ == "__main__":
    print(main())
