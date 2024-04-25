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
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w', delete=False) as tmpfile:
    ...    _ = tmpfile.write('ABBE 1 AE1 B IY0\\n\
ABBE 2 AE0 B EY1\\n\
ABBOUD 1 AH0 B UW1 D\\n\
ABBOUD 2 AH0 B AW1 D\\n\
NACHOS 1 N AA1 CH OW0 Z\\n\
NACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_tuple(tmpfile.name)
    [('ABBE', 1, ['AE1', 'B', 'IY0']), ('ABBE', 2, \
['AE0', 'B', 'EY1']), ('ABBOUD', 1, ['AH0', 'B', 'UW1', 'D']), \
('ABBOUD', 2, ['AH0', 'B', 'AW1', 'D']), ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z']), \
('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z'])]
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
        result = {}
        for group in super_list:
            key = group[0]
            value = tuple(group[2])
            if key in result:
                result[key].add(value)
            else:
                result[key] = {value}
        return result
    return None


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
    {1: {('ABBE', (('AE1', 'B', 'IY0'),))}}
    '''
    if isinstance(dct, dict):
        dct = {key : tuple(value) for key, value in dct.items()}
        lengths = {len(transcriptions) for transcriptions in dct.values()}
        result = {length: [] for length in lengths}
        for word, transcriptions in dct.items():
            length = len(transcriptions)
            result[length].append((word, transcriptions))
        result = {key : set(value) for key, value in result.items()}
        return dict(sorted(result.items()))
    if isinstance(dct, list):
        pass
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
