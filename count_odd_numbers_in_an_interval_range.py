class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Counts the number of odd integers within the inclusive interval [low, high].

        Args:
            low (int): The lower bound of the interval.
            high (int): The upper bound of the interval.

        Returns:
            int: The count of odd numbers between low and high, inclusive.

        Example:
            Input: low = 3, high = 7
            Output: 3  # (3, 5, 7)

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 96.00% of submissions
        """
        first_odd = low if low % 2 == 1 else low + 1
        last_odd = high if high % 2 == 1 else high - 1

        return (last_odd - first_odd) // 2 + 1
