'''Example'''
EXAMPLE = (20, 15)

def create_table(n, m, lst = None):
    '''fff'''
    if lst is None:
        lst = [1]*m
    table = [list(lst)]
    for _ in range(1, n):
        for i in range(1, m):
            lst[i] += lst[i-1]
        table.append(list(lst))
    return table