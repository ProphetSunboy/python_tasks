class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        """Check if two strings are almost equivalent based on letter frequency differences.

        Two strings word1 and word2 are considered almost equivalent if the differences
        between the frequencies of each letter from 'a' to 'z' between word1 and word2
        is at most 3.

        Args:
            word1 (str): First string to compare, consisting of lowercase English letters.
            word2 (str): Second string to compare, consisting of lowercase English letters.

        Returns:
            bool: True if word1 and word2 are almost equivalent, False otherwise.

        Example:
            >>> checkAlmostEquivalent("aaaa", "bccb")
            False
            >>> checkAlmostEquivalent("abcdeef", "abaaacc")
            True
            >>> checkAlmostEquivalent("cccddabba", "babababab")
            True

        Time complexity: O(n) where n is the total length of both strings
        Space complexity: O(1) since we use fixed-size dictionaries for 26 letters

        LeetCode: Beats 100% of submissions
        """
        c_1 = Counter(word1)
        c_2 = Counter(word2)

        for l, freq in c_1.items():
            if abs(freq - c_2.get(l, 0)) > 3:
                return False

        for l, freq in c_2.items():
            if abs(freq - c_1.get(l, 0)) > 3:
                return False

        return True
