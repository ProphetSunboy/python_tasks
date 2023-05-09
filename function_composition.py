from functools import reduce

def compose2(f, g):
    '''
    Calls function g on inputs, then function f on results
    '''
    return lambda *a, **kw: f(g(*a, **kw))

def compose(*fs):
    '''
    Reduces given inputs to a single value by calling input functions 
    '''
    return reduce(compose2, fs)