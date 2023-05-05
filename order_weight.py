def order_weight(strng):
    '''
    Function recieves string of numbers, separated by white spaces
    and return sorted string of numbers.
    Sorting is performed by the sum of digits of numbers in ascending order.
    When two numbers have the same "weight", sort is done in alphabetical order.
    '''
    return ' '.join(sorted(sorted(strng.split()), key=lambda x: sum(map(int, list(x)))))