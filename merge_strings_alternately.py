class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the strings by adding
        letters in alternating order, starting with word1. If a string is longer
        than the other, append the additional letters onto the end of the merged
        string.

        Return the merged string.

        :param str word1: string of letters
        :param str word2: string of letters
        :returns str res: merge of word1 and word2

        Time complexity: O(n)
        Space complexity: O(n + m)


        LeetCode: Beats 95.95%
        """
        res = ""

        for x, y in zip(word1, word2):
            res += x + y

        res += word1[len(word2) :] + word2[len(word1) :]

        return res
