'''Algorithms'''

import random

EXAMPLE_SEARCH = ([1, 2, 3, 4, 5, 6], 3)
EXAMPLE_SORT = [5, 1, 23, 4, 5, 6]


def linear_search(list_of_values: list, value: int)-> int:
    """
    Perform linear search on a list to find the index of a given value.

    >>> linear_search([1, 2, 3, 4, 5, 6], 3)
    2
    >>> linear_search([1, 2, 3, 4, 5, 6], 7)
    -1
    """
    # Short-circuit the loop if the value is the first element (common case)
    if list_of_values and list_of_values[0] == value:
        return 0
    for i, lstvalue in enumerate(list_of_values[1:]):  # Skip the first element
        if value == lstvalue:
            return i + 1  # Adjust index for skipping the first element
    return -1

def binary_search(list_of_values: list, value: int)-> int:
    """
    Perform binary search on a sorted list to find the index of a given value.

    >>> binary_search([1, 2, 3, 4, 5, 6], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5, 6], 7)
    -1
    """
    left, right = 0, len(list_of_values) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == list_of_values[mid]:
            return mid
        if value < list_of_values[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def selection_sort(lst:list)-> list:
    """
    Sort list by selection sort method.

    >>> selection_sort([5,1,23,4,5,6])
    [1, 4, 5, 5, 6, 23]
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]  # Swap elements in-place
    return lst

def merge_sort(lst:list)-> list:
    """
    Sort list by merge sort method.

    >>> merge_sort([5,1,23,4,5,6])
    [1, 4, 5, 5, 6, 23]
    >>> merge_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left: list, right: list)-> list:
    """
    Merge two sorted lists into a single sorted list.
    """
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]  # Add remaining elements from left list
    merged += right[j:]  # Add remaining elements from right list
    return merged

def quick_sort(lst:list)-> list:
    """
    Sort list by quicksort method using randomized pivot selection and Lomuto partition scheme.

    >>> quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5])
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    """
    if len(lst) <= 1:
        return lst
    # Randomly select a pivot element
    pivot_index = random.randint(0, len(lst) - 1)
    lst[0], lst[pivot_index] = lst[pivot_index], lst[0]  # Move pivot to the first element
    pivot = lst[0]
    i = 1  # Index for elements less than pivot
    for j in range(1, len(lst)):
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[0], lst[i - 1] = lst[i - 1], lst[0]  # Move pivot to its final position
    left = quick_sort(lst[:i - 1])
    right = quick_sort(lst[i:])
    return left + [pivot] + right
