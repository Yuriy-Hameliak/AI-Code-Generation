"""
https://www.codewars.com/kata/660e5631b673a8004b71d208/train/python
"""
def continued_fraction(numerator, denominator):
  """
  Calculates the continued fraction of a fraction.

  Args:
      numerator: The numerator of the fraction.
      denominator: The denominator of the fraction.

  Returns:
      A list representing the continued fraction.
  """
  if numerator == 0:
    return []

  result = []
  while denominator > 0:
    result.append(numerator // denominator)
    numerator %= denominator
    numerator, denominator = denominator, numerator  # Swap for efficiency
  return result
  
