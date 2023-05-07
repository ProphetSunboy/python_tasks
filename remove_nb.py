def remov_nb(n):
    '''
    Within sequence from 1 to n, function return all groups
    of two numbers, a and b, so that the product of a and b
    should be equal to the sum of all numbers in the sequence,
    excluding a and b.
    '''
    res = []
    a = sum(range(1, n+1))
    for i in range(n//2, n+1):
        val = (a - i * 2) // i
        if i * val == a - i - val:
            res.append((i, val))
        if i * (val + 1) == a - i - (val+1):
            res.append((i, val+1))
    return res