def isValid(self, s: str) -> bool:
    '''
    Given a string s containing just the characters '(', ')', '{', '}',
    '[' and ']', return if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    '''
    seen = []
    for ch in s:
        if seen == [] and ch in ')]}':
            return False
        if ch in '([{': seen.append(ch)
        if ch in ')]}':
            if ord(ch) - ord(seen.pop()) not in (1,2): return False

    return True if seen == [] else False