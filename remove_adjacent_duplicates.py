def removeDuplicates(s: str) -> str:
    """
    Given a string s consisting of lowercase English letters.
    A duplicate removal consists of choosing two adjacent and equal letters
    and removing them.

    Repeatedly removes duplicates in s until there is no duplicates in s.

    Return the final string after all such duplicate removals have been made.
    """
    stack = []
    for le in s:
        if stack and stack[-1] == le:
            stack.pop()
        else:
            stack.append(le)
    return "".join(stack)