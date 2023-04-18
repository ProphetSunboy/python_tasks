def evaluate(equation):
    """
    New operator, @, which is left associative.
    a @ b = (a + b) + (a - b) + (a * b) + (a // b)
    """
    oper = list(map(int, equation.split(' @ ')))
    try:
        res = 2 * oper[0] + oper[0] * oper[1] + oper[0] // oper[1]
        for num in oper[2:]:
            res = 2 * res + res * num + res // num
        
        return res
    except ZeroDivisionError:
        return None