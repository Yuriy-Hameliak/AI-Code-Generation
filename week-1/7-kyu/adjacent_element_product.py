'''https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python'''

def adjacent_element_product(arr):
    """
    Finds the maximum product obtained from multiplying 2 adjacent numbers in the array.

    Args:
      arr: A list of integers.
    
    Returns:
      The maximum product obtained from multiplying 2 adjacent numbers in the array.
    """

    max_product = float('-inf')  # Initialize max_product to negative infinity
    for i in range(len(arr) - 1):
        product = arr[i] * arr[i + 1]
        max_product = max(max_product, product)  # Update max_product if a larger product is found

    return max_product
