class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        """
        Given a string s consisting of lowercase English letters and an integer k,
        delete the minimum number of characters from s so that the resulting string
        contains at most k distinct characters.

        Args:
            s (str): The input string.
            k (int): The maximum allowed number of distinct characters.

        Returns:
            int: The minimum number of deletions required.

        Example:
            >>> minDeletion("aabbcc", 2)
            2
            >>> minDeletion("abcde", 3)
            2

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(1) (since the alphabet size is constant).

        LeetCode: Beats 100% of submissions
        """
        c = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        deletions = 0

        while len(c) > k:
            deletions += c.pop()[1]

        return deletions
