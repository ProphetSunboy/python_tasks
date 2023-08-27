class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        Given two strings a and b, return the length of the longest uncommon
        subsequence between a and b.
        If the longest uncommon subsequence does not exist, return -1.

        An uncommon subsequence between two strings is a string that is a
        subsequence of one but not the other.

        A subsequence of a string s is a string that can be obtained after
        deleting any number of characters from s.

            For example, "abc" is a subsequence of "aebdc" because you can
            delete the underlined characters in "aebdc" to get "abc". Other
            subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


        :param str a: string of English letters
        :param str b: string of English letters
        :returns int longest_sub: length of longest uncommon subsequence

        Time complexity: θ(n)
        Space complexity: O(1)

        LeetCode: Beats 97.80%
        """
        if len(a) != len(b):
            return max(len(a), len(b))

        if a != b:
            return len(a)
        else:
            return -1
