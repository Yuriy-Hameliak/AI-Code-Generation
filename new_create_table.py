'''Example'''
EXAMPLE = (20, 15)

def create_table(n, m, lst=None):
    """
    Function for creating table for a game
    >>> create_table(4,6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    if lst is None:
        lst = [1]*m
    table = [list(lst)]
    for _ in range(1, n):
        for i in range(1, m):
            lst[i] += lst[i-1]
        table.append(list(lst))
    return table