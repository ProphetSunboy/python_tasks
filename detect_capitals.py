class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Given a string word, return True if the usage of capitals in it is right.

        We define the usage of capitals in a word to be right when one of the
        following cases holds:

            All letters in this word are capitals, like "USA".
            All letters in this word are not capitals, like "leetcode".
            Only the first letter in this word is capital, like "Google".

        :param str word: word, where we search capitals
        :returns bool ans: search result

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 97.35%
        """
        if word.isupper() or word.islower():
            return True

        up = 0

        for ch in word:
            if ch.isupper():
                up += 1

        return up == 1 and word[0].isupper()
