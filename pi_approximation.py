from math import pi

def iter_pi(epsilon):
    """
    Return the approximate value of pi, given a precision of epsilon.
    """
    seq_sum = 0
    divider = 1
    iter = 0
    while abs(seq_sum * 4 - pi) >= epsilon:
        if iter % 2:
            seq_sum += -1/divider
        else:
            seq_sum += 1/divider
        divider += 2
        iter += 1
    return [iter, round(seq_sum * 4, 10)]