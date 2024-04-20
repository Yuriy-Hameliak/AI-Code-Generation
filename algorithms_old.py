'''Algorithms'''

def linear_search(list_of_values: list,value: int)-> int:
    '''
    Perform linear search on a list to find the index of a given value.

    >>> linear_search([1, 2, 3, 4, 5, 6], 3)
    2
    >>> linear_search([1, 2, 3, 4, 5, 6], 7)
    -1
    '''
    for i, lstvalue in enumerate(list_of_values):
        if value==lstvalue:
            return i
    return -1

def binary_search(list_of_values: list,value: int)-> int:
    '''
    Perform binary search on a sorted list to find the index of a given value.

    >>> binary_search([1, 2, 3, 4, 5, 6], 3)
    2
    >>> binary_search([1, 2, 3, 4, 5, 6], 7)
    -1
    '''
    left, right=0, len(list_of_values)-1
    while left<=right:
        mid=(left+right)//2
        if value==list_of_values[mid]:
            return mid
        if value<list_of_values[mid]:
            right=mid-1
        else:
            left=mid+1
    return -1

def selection_sort(lst:list)-> list:
    '''
    Sort list by selection sort method.
    
    >>> selection_sort([5,1,23,4,5,6])
    [1, 4, 5, 5, 6, 23]
    >>> selection_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''
    return_lst=[]
    while len(lst):
        return_lst.append(min(lst))
        lst.remove(min(lst))
    return return_lst

def merge_sort(lst:list)-> list:
    '''
    Sort list by merge sort method.

    >>> merge_sort([5,1,23,4,5,6])
    [1, 4, 5, 5, 6, 23]
    >>> merge_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''
    if len(lst)>1:
        mid=len(lst)//2
        l_half=lst[:mid]
        r_half=lst[mid:]
        merge_sort(l_half)
        merge_sort(r_half)
        i, j, l=0, 0, 0
        result=[None]*len(lst)
        while i<len(l_half) and j<len(r_half):
            if l_half[i]<r_half[j]:
                result[l]=l_half[i]
                i+=1
            else:
                result[l]=r_half[j]
                j+=1
            l+=1
        while i<len(l_half):
            result[l]=l_half[i]
            i, l=i+1, l+1
        while j<len(r_half):
            result[l]=r_half[j]
            j, l=j+1, l+1
        for i, _ in enumerate(lst):
            lst[i]=result[i]
    return lst

def quick_sort(lst:list)-> list:
    '''
    Sort list by qsort method

    >>> quick_sort([5,1,23,4,5,6])
    [1, 4, 5, 5, 6, 23]
    >>> quick_sort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''
    if lst==[]:
        return lst
    pivot=lst.pop(0)
    l_half=list(filter(lambda x:x<=pivot,lst))
    r_half=list(filter(lambda x:x>pivot,lst))
    return quick_sort(l_half) + [pivot] + quick_sort(r_half)
