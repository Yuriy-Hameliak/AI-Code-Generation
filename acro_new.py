'''
AI improved version: of "Creating and explaining acronyms"
Interesting fact:
AI stole it from:
https://github.com/OlehPalka/First_semester_labs
'''

EXAMPLE = 'random access memory\nAs soon As possible'

def create_acronym(message: str) -> str:
    """
    Function to create acronyms from phrases separated by newline characters.

    >>> create_acronym('random access memory\\nAs soon As possible')
    'RAM - random access memory\\nASAP - As soon As possible'
    >>> create_acronym("661816")

    >>> create_acronym("661816\\n7089")

    """

    if not isinstance(message, str):
        return None

    lines = message.split("\n")
    acronyms = []
    for line in lines:
        if not line.strip():  # Check if line is empty
            continue

        if not line.replace(" ", "").isalpha():  # Check if line contains only letters
            return None

        words = line.split()
        acronym = "".join(word.capitalize()[0] for word in words)
        acronyms.append(acronym)

    result = "\n".join(f"{acronym} - {''.join(words)}" for acronym, words in zip(acronyms, lines))
    return result
