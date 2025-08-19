class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Returns the number of sublists in the input list that are filled entirely with 0.

        A sublist is a contiguous, non-empty sequence of elements within the list.

        Args:
            nums (list[int]): List of integers.

        Returns:
            int: The total number of sublists consisting only of zeros.

        Example:
            >>> zeroFilledSubarray([0, 0, 0, 2, 0, 0])
            9

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 99.61% of submissions
        """
        zero_f = 0
        curr_z = 0

        for num in nums:
            if num == 0:
                curr_z += 1
            else:
                zero_f += (curr_z * (curr_z + 1)) // 2
                curr_z = 0

        zero_f += (curr_z * (curr_z + 1)) // 2

        return zero_f
