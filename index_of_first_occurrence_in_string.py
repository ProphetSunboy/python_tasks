def strStr(self, haystack: str, needle: str) -> int:
    '''
    Given two strings needle and haystack, returns the index
    of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    '''
    if len(needle) > len(haystack): return -1
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle: return i
    return -1