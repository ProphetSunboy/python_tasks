class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        """
        Given two sentences s1 and s2, return a list of all the uncommon words.
        You may return the answer in any order.

        A sentence is a string of single-space separated words where each word
        consists only of lowercase letters.

        A word is uncommon if it appears exactly once in one of the sentences,
        and does not appear in the other sentence.

        :param str s1: lowercase string
        :param str s2: lowercase string
        :returns list[str] ans: list of the uncommon words from s1 and s2

        Time complexity: O(n+m)
        Space complexity: O(n+m)

        LeetCode: Beats 99.92%
        """
        words = collections.Counter((s1 + " " + s2).split())
        ans = set()

        for word, freq in words.items():
            if freq == 1:
                ans.add(word)

        return ans
