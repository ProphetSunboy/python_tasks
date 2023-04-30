def next_item(xs, item):
    '''
    Given a sequence of items xs and a specific item, return the item
    immediately following the item specified. If the item occurs more
    than once in a sequence, return the item after the first occurence.
    Function work for a sequence of any type.
    When the item isn't present or nothing follows it, the function return None.
    '''
    try:
        for i, el in enumerate(xs):
            if el == item and i != len(xs)-1:
                return xs[i+1]
    except TypeError:
        return next(xs)