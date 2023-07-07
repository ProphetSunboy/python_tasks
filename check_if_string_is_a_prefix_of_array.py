class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        """
        Given a string s and an array of strings words, determine whether s is
        a prefix string of words.

        A string s is a prefix string of words if s can be made by concatenating
        the first k strings in words for some positive k no larger
        than len(words).

        Return True if s is a prefix string of words, or False otherwise.
        """
        prefix = ''

        for word in words:
            prefix += word

            if prefix != s[:len(prefix)]:
                return False   

            if prefix == s:
                return True
            
        return False