class Solution:
    def maxDifference(self, s: str) -> int:
        """Finds the maximum difference between frequencies of characters with odd and even counts.

        Given a string s of lowercase English letters, finds the maximum difference between:
        - freq(a1): frequency of a character with odd count
        - freq(a2): frequency of a character with even count

        Args:
            s (str): Input string of lowercase English letters

        Returns:
            int: Maximum difference between frequencies (freq(a1) - freq(a2)) where:
                - a1 is a character with odd frequency
                - a2 is a character with even frequency

        Example:
            >>> maxDifference("aabbbcc")
            1  # 'b' has odd freq(3), 'a' has even freq(2), difference is 3-2=1

        Time complexity: O(n) - where n is length of string
        Space complexity: O(1) - since we only store counts for lowercase letters

        LeetCode: Beats 100% of submissions
        """
        count = Counter(s)

        a1 = 0
        a2 = 101
        for val in count.values():
            if val % 2 and val > a1:
                a1 = val
            elif val % 2 == 0 and val < a2:
                a2 = val

        return a1 - a2
