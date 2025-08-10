class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Determines if the digits of the given integer n can be reordered (without leading zeros) to form a power of two.

        Args:
            n (int): The integer whose digits are to be checked.

        Returns:
            bool: True if the digits of n can be reordered to form a power of two, False otherwise.

        Example:
            >>> reorderedPowerOf2(1)
            True
            >>> reorderedPowerOf2(16)
            True
            >>> reorderedPowerOf2(18)
            False

        Time Complexity: O(1) - since the number of possible powers of two within 32-bit integer range is constant.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        nums = []

        for i in range(31):
            nums.append(Counter(str(2**i)))

        return Counter(str(n)) in nums
