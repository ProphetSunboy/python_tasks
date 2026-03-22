class Solution:
    def countCommas(self, n: int) -> int:
        """
        Returns the total number of commas used when writing all integers
        from 1 to n (inclusive) in standard number formatting.

        Standard formatting places a comma after every three digits from
        the right. Numbers with fewer than four digits contain no commas.

        Args:
            n (int): The upper bound integer.

        Returns:
            int: The total number of commas used.

        Example:
            Input: n = 1002
            Output: 3

        Time Complexity: O(1).
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        return max(0, n - 999)
