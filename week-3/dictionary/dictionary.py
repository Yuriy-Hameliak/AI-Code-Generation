'''
Module for reading and inverting dictionary.
'''

def dict_reader_tuple(file_dict: str) -> list[tuple]:
    '''
    str -> list[tuple]
    Reads the dictionary file and
    returns list of tuples, which consist
    of word, its translation number and
    translation itself.
    '''
    if isinstance(file_dict, str):
        with open(file_dict, 'r+', encoding='utf-8') as words:
            result = [tuple([line.split()[0], int(line.split()[1]),
                            [line.split()[k] for k in range(2, len(line.split()))]])
                      for line in [f.strip() for f in words.readlines()]]
        return result
    return None


def dict_reader_dict(file_dict: str) -> dict:
    '''
    str -> dict
    Reads the dictionary file and
    returns dictionary with word as
    a key and set of all its
    transcriptions as value.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...    _ = tmpfile.write('ABBE 1 AE1 B IY0\\nABBE 2 AE0 B EY1')
    >>> elements = dict_reader_dict(tmpfile.name)
    >>> ('AE0', 'B', 'EY1') in elements['ABBE'] and ('AE1', 'B', 'IY0') in elements['ABBE'] \
and len(elements['ABBE']) == 2
    True
    '''
    if isinstance(file_dict, str):
        super_list = dict_reader_tuple(file_dict)
    else:
        super_list = file_dict
    result = {}
    for group in super_list:
        key = group[0]
        value = tuple(group[2])
        if key in result:
            result[key].add(value)
        else:
            result[key] = {value}
    return result


def dict_invert(dct: dict|list[tuple]) -> dict:
    '''
    dict | list[tuple] -> dict
    Returns a dictionary
    whose keys are the number of pronunciations, and
    whose values are sets of tuples, where a tuple
    represents a word that has the number of
    pronunciations equal to the key. Each tuple has two
    elements - a string (word) and a tuple (sound syllables).
    The argument when calling this function must be the object
    returned by the dict_reader_tuple(file_dict) or
    dict_reader_dict(file_dict) function.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...    _ = tmpfile.write('ABBE 1 AE1 B IY0')
    >>> dict_invert(dict_reader_dict(tmpfile.name))
    {1: {('ABBE', ('AE1', 'B', 'IY0'))}}
    '''
    dictionary = {}
    if isinstance(dct, list):
        dct = dict_reader_dict(dct)
    for i in dct:
        numb = len(list(dct[i]))
        words = set((i, (j)) for j in dct[i])
        dictionary[numb] = words
    return dict(sorted(dictionary.items(), key=lambda item: item[0]))
