'''
LINK:
https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
'''

class CaesarCipher:
    def __init__(self, shift):
        """
        Initializes a CaesarCipher object with a shift value.

        Args:
            shift (int): The number of positions to shift letters by.
        """

        self.shift = shift % 26  # Ensure shift stays within 1-26

    def encode(self, message):
        """
        Encodes a message using the Caesar Cipher.

        Args:
            message (str): The message to encode.

        Returns:
            str: The encoded message.
        """

        result = ""
        for char in message:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')  # Base ASCII code for uppercase/lowercase
                # shifted_index = (ord(char) - base + self.shift) % 26 - incorrect line
                shifted_index = (ord(char) - base + self.shift) % 26
                # Handle wrapping for all letters
                ###################################################
                # new_index = (shifted_index + base - 1) % 26 + 1 #
                # WRONG LINE, THERE IS NO NEED IN %26 HERE        #
                ###################################################
                new_index = (shifted_index + base)  # Ensure proper wrapping
                new_char = chr(new_index)
                result += new_char.upper()
            else:
                result += char  # Keep non-alphabetic characters as is
        return result

    def decode(self, message):
        """
        Decodes a message using the Caesar Cipher.

        Args:
            message (str): The message to decode.

        Returns:
            str: The decoded message.
        """

        # return self.encode(-self.shift) - WRONG
        # Decode by encoding with negative shift
        self.shift *= -1
        result = self.encode(message)
        self.shift *= -1
        return result
