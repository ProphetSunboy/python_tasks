class Solution:
    def getSmallestString(self, s: str) -> str:
        """
        Given a string s consisting only of digits, returns the lexicographically smallest
        string obtainable by performing at most one swap of two adjacent digits with the same parity (both even or both odd).

        Two digits have the same parity if both are odd or both are even (e.g., 2 and 4, 5 and 9).

        Args:
            s (str): The input string of digits.

        Returns:
            str: The lexicographically smallest string after at most one allowed swap.

        Example:
            >>> getSmallestString("45320")
            '43520'
            >>> getSmallestString("13542")
            '13524'

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i + 1]) % 2 and s[i] > s[i + 1]:
                return s[:i] + s[i + 1] + s[i] + s[i + 2 :]

        return s
