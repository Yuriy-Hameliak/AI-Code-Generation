"""
This program prints a pattern of characters based on a given number.
The pattern starts with 'A' and increases alphabetically until the input number is reached.

Example:
Input: 7
Output:
      A
    B C
  D E F
G
"""
EXAMPLE = 7
def main(n):
    """f"""
    NUM = int(input()) if not n else n
    N = 0
    L = 0
    C = 0

    while N < NUM:
        L += 1
        N += L

    for i in range(1, L + 1):
        print('  ' * (L - i), end='')

        chars = (chr(65 + C) for C in range(C, min(C + i, NUM)))
        print(' '.join(chars))

        C += i
        if C >= NUM:
            break
