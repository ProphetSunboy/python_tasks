class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of words and spaces, return the length of
        the last word in the string.

        A word is a maximal substring consisting of non-space characters only.

        Constraints:

            1 <= s.length <= 104
            s consists of only English letters and spaces ' '.
            There will be at least one word in s.

        LeetCode: Beats 90.97%
        """
        length = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                continue
            else:
                while s[i] != ' ' and i >= 0:
                    length += 1
                    i -= 1
                
                return length