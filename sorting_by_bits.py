def sort_by_bit(arr):
    '''
    Function sorts an array of 32-bit integers in ascending
    order of the number of on bits they have.
    In cases where two numbers have the same number of bits,
    compare their real values instead.
    Function sort array in place.
    Return None
    '''
    arr.sort()
    arr.sort(key=lambda x: bin(x).count('1'))