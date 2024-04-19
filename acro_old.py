'''Creating and explaining acronyms'''

def create_acronym(message: str) -> str:
    '''
    str -> str
    Function create_acronym(message) which receives the feed,
    consisting of phrases separated by a newline character,
    as an argument, and returns the acronyms for those phrases.
    >>> create_acronym('random access memory\\nAs soon As possible')
    'RAM - random access memory\\nASAP - As soon As possible'
    >>> create_acronym("661816")

    >>> create_acronym("661816\\n7089")
    
    '''
    if isinstance(message, str):
        lines = message.split("\n")
        acronyms = []
        for _ in lines:
            for check in _:
                if check.isdigit():
                    return None
        result = ""
        for number, sentence in enumerate(lines):
            acronyms.append("".join([k.capitalize()[0] for k in sentence.split()]))
            result += f"{acronyms[number]} - {sentence}"
            if number != len(lines) - 1:
                result += "\n"
        return result
    return None
