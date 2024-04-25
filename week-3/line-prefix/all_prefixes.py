"""A"""


def all_prefixes(line):
    """s"""
    if isinstance(line, str):
        if line:
            res = []
            for i in range(l := len(line)):
                if line[i] == line[0]:
                    for m in range(i, l):
                        res.append(line[i:m+1])
            return set(res)
        return 'Empty line'
    raise TypeError
