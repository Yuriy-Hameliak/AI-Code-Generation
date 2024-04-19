'''Ceasar code'''
def caesar_encode(message: str, key: int) -> str:
    '''
    (str, int) -> str
    Function consists in moving each letter of the plain text of the message
    by a fixed number (called a key) of positions in the alphabet ahead.
    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    >>> caesar_encode(84646, 3)

    >>> caesar_encode("z", 1)
    'a'
    '''
    if all([isinstance(message, str), isinstance(key, int)]):
        upper_alphabet = "".join([chr(k) for k in range(97,123)])
        lower_alphabet = "".join([chr(k) for k in range(65,91)])
        result = ""
        for element in message:
            if element in upper_alphabet:
                pos = upper_alphabet.index(element)
                result += upper_alphabet[(pos + key) % 26]
            elif element in lower_alphabet:
                pos = lower_alphabet.index(element)
                result += lower_alphabet[(pos + key) % 26]
            else:
                result += element
        return result
    return None

def caesar_decode(message: str, key: int) -> str:
    '''
    (str, int) -> str
    Function consists in moving each letter of the plain text of the message
    by a fixed number (called a key) of positions in the alphabet backwards.
    >>> caesar_decode("frpsxwhu", 3)
    'computer'
    >>> caesar_decode(84646, 3)

    >>> caesar_decode("a", 1)
    'z'
    '''
    if all([isinstance(message, str), isinstance(key, int)]):
        upper_alphabet = "".join([chr(k) for k in range(97,123)])
        lower_alphabet = "".join([chr(k) for k in range(65,91)])
        result = ""
        for element in message:
            if element in upper_alphabet:
                pos = upper_alphabet.index(element)
                result += upper_alphabet[(pos - key) % 26]
            elif element in lower_alphabet:
                pos = lower_alphabet.index(element)
                result += lower_alphabet[(pos - key) % 26]
            else:
                result += element
        return result
    return None
