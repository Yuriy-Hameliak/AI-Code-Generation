def neutralise(str1, str2):
    '''Function that takes two strings and returns a string containing only the characters \
that are the same in both strings. If there are no matching characters, return an empty string.'''
    result = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            result += str1[i]  # Positives with positives or negatives with negatives
        else:
            result += "0"  # Positives with negatives become neutral (0)
    return result
