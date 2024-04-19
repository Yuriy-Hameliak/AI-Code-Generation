'''https://www.codewars.com/kata/546e2562b03326a88e000020/train/python'''

def square_digits(num):
    """Squares every digit of a number and concatenates them.

    Args:
      num: An integer.

    Returns:
      An integer with the squared digits concatenated.
    """

    return int(''.join(str(int(d) ** 2) for d in str(num)))
