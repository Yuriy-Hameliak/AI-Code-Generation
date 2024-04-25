def flick_switch(items):
    '''Flick the switch on "flick" encounters, return the state of the switch after each flick.'''
    is_flipped = True  # Flag to track if flipping is active
    results = []
    for item in items:
        if item == "flick":
            is_flipped = not is_flipped  # Toggle flipping on "flick" encounters
        results.append(is_flipped)
    return results
