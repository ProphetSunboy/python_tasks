def autocomplete(input_, dictionary):
    """
    Take in an input string and a dictionary array and return the values
    from the dictionary that start with the input string.
    """
    inp = ''.join(ch for ch in input_ if ch.isalpha())
    return [word for word in dictionary if word.lower().startswith(inp)][:5]