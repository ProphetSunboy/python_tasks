class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        """
        Given a string s and an integer k, reverse the first k characters of s
        and return the resulting string.

        Args:
            s (str): The input string.
            k (int): The number of characters to reverse from the start.

        Returns:
            str: The string with its first k characters reversed.

        Example:
            Input: s = "abcdefg", k = 3
            Output: "cbadefg"

        Time Complexity: O(k), where k is the number of characters to reverse.
        Space Complexity: O(k), due to the slicing and reversing of the prefix.

        LeetCode: Beats 100% of submissions
        """
        return s[:k][::-1] + s[k:]
