def mul_by_n(lst, n):
    '''Return a list of the input list multiplied by n.'''
    print("Inputs: ", lst, n) # Check our inputs
    result_list = []
    for item in lst:
        result_list.append(item * n)
    print("Result: ", list(result_list)) # Check our result
    return list(result_list)
