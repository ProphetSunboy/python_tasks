class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        """
        You are given a 0-indexed list of strings words and a character x.

        Return a list of indices representing the words that contain the
        character x.

        :param list[str] words: list of lowercase words
        :param str x: lowercase letter
        :returns list[int]: list of indices representing the words that contain
        the character x

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 100%
        """
        return [i for i, word in enumerate(words) if x in word]