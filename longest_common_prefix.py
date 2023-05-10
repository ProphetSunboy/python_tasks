def longestCommonPrefix(self, strs: List[str]) -> str:
    '''
    Find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    '''
    if not all(bool(s) for s in strs):
        return ''

    pref = strs[0][0]
    if not all(s.startswith(pref) for s in strs):
        return ''

    for i in range(1, len(strs[0])+1):
        new_pref = strs[0][:i]
        if not all(s.startswith(new_pref) for s in strs):
            return pref
        pref = new_pref
    return pref