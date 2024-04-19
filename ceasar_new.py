'''Ceasar code'''

EXAMPLE = ("This is a very long message to test the \
Caesar cipher functionality. It contains a mix of \
uppercase and lowercase letters to ensure proper \
encoding and decoding across the entire alphabet. \
The message length is designed to be quite large to \
push the boundaries of the code and identify potential \
performance issues. By using such a test case, we can \
gain confidence in the robustness of the Caesar cipher \
implementation.", 5)

def caesar_encode(message: str, key: int) -> str:
    """
    Encodes a message using Caesar cipher.

    Args:
        message: The message to encode.
        key: The shift value.

    Returns:
        The encoded message.

    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    >>> caesar_encode(84646, 3)

    >>> caesar_encode("z", 1)
    'a'
    """
    if not isinstance(message, str):
        return None  # Handle non-string message

    if not isinstance(key, int):
        return None  # Handle non-integer key

    result = ''
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + key) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

def caesar_decode(message: str, key: int) -> str:
    """
    Decodes a message using Caesar cipher.

    Args:
        message: The message to decode.
        key: The shift value.

    Returns:
        The decoded message.

    >>> caesar_decode("frpsxwhu", 3)
    'computer'
    >>> caesar_decode(84646, 3)

    >>> caesar_decode("a", 1)
    'z'
    """
    return caesar_encode(message, -key)  # Reuse encode with negative key for decode

if __name__ == '__main__':
    import doctest
    doctest.testmod()
