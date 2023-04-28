def chain(val, functions):
    '''
    Function chainer that takes a starting value, and an array of functions
    to execute on it.
    The input for each function is the output of the previous function. 
    Returns the final value after execution is complete.
    '''
    for func in functions:
        val = func(val)
    return val