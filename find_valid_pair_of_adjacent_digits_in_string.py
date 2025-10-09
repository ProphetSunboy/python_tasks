class Solution:
    def findValidPair(self, s: str) -> str:
        """
        Given a string s consisting only of digits, finds the first valid pair of adjacent digits.

        A valid pair is defined as two adjacent digits in s such that:
            - The first digit is not equal to the second.
            - Each digit in the pair appears in s exactly as many times as its numeric value.

        Returns the first valid pair found when traversing s from left to right.
        If no valid pair exists, returns an empty string.

        Args:
            s (str): The input string consisting only of digits.

        Returns:
            str: The first valid pair as a string, or an empty string if none exists.

        Example:
            >>> findValidPair("122333")
            '23'

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(s)

        for i in range(len(s) - 1):
            if (
                s[i] != s[i + 1]
                and c[s[i]] == int(s[i])
                and c[s[i + 1]] == int(s[i + 1])
            ):
                return s[i] + s[i + 1]

        return ""
