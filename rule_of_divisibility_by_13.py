def thirt(n):
    '''
    When you divide the successive powers of 10 by 13 you get 
    the following remainders of the integer divisions:
        [1, 10, 9, 12, 3, 4].
    Function multiply
        the right most digit of the number with the left most number
        in the sequence shown above,
        the second right most digit with the second left most digit
        of the number in the sequence.
    The cycle goes on and sum all these products.
    This process repeats until the sequence of sums is stationary.
    '''
    divisors = [1, 10, 9, 12, 3, 4] * 10
    old = n-1
    new = n
    while old != new:
        old = new
        new = sum(num * divisors[i] for i, num in enumerate(map(int, str(new)[::-1])))
    return new