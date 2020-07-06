# Longest Collatz sequence
def generate_sequence(n):
    seq = [n]
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = n*3+1
        seq.append(n)
    return seq

def main():
    max_seq_len = 0
    num = 0
    for i in range(1000001):
        seq_len = len(generate_sequence(i))
        if seq_len > max_seq_len:
            num = i
            max_seq_len = seq_len
    return num

if __name__ == "__main__":
    print(main())
