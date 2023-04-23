def longest_palindrome (s):
    """
    def longest_palindrome(s):
    
    Return the length of the longest substring in the given string s that is the
    same in reverse. 
    """
    max_pal = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > max_pal:
                max_pal = len(s[i:j])
                
    return max_pal