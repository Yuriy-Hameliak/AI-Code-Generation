def best_friend(text, letter1, letter2):
    '''Best friend function that checks if a letter is \
always followed by another letter in a text.'''
    i = 0
    expected_letter = letter2  # Initialize with the second letter
    while i < len(text):
        if text[i] == letter1:
            if i + 1 >= len(text) or text[i + 1] != expected_letter:
                return False  # Letter1 not followed by letter2
            expected_letter = text[i + 1]  # Update expected letter for next iteration
        i += 1
    return True
