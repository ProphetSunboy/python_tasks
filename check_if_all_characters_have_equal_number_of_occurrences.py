class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """Check if all characters in a string have equal number of occurrences.

        Args:
            s (str): Input string to check

        Returns:
            bool: True if all characters appear the same number of times, False otherwise

        Examples:
            >>> areOccurrencesEqual("abacbc")
            True  # 'a': 2, 'b': 2, 'c': 2
            >>> areOccurrencesEqual("aaabb")
            False  # 'a': 3, 'b': 2

        Time complexity: O(n) - where n is length of string
        Space complexity: O(k) - where k is number of unique characters

        LeetCode: Beats 100% of submissions
        """
        c = Counter(s)

        checker = c[s[0]]

        goodness = True
        for val in c.values():
            if val != checker:
                goodness = False

        return goodness
