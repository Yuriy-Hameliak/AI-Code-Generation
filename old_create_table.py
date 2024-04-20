def create_table(n, m, lst = None):
    """
    Function for creating table for a game
    >>> create_table(4,6) 
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    if lst is None:
        return create_table(n, m, [1]*m)
    upper_row = lst
    table = [lst]
    for current_row in range(1, n):
        current_row = [1]
        for elem in range(1, m):
            current_row.append(upper_row[elem]+current_row[elem-1])
        upper_row = current_row
        table.append(current_row)
    return table