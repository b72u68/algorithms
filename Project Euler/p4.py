# Largest palindrome product
def check_palindrome(n):
    if len(n) < 2:
        return True
    else:
        last_digit = n[-1]
        first_digit = n[0]
        if first_digit == last_digit:
            return check_palindrome(n[1:-1])
        else:
            return False

def main():
    palindrome_int = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if check_palindrome(str(i*j)):
                palindrome_int.append(i*j)
    return max(palindrome_int)

if __name__ == "__main__":
    print(main())
