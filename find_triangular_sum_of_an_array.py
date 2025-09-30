class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        Calculates the triangular sum of a 0-indexed integer list `nums`,
        where each element is a digit between 0 and 9.

        The triangular sum is obtained by repeatedly replacing the list with a
        new list where each element is the sum of adjacent elements modulo 10,
        until only one element remains.

        Process:
            1. While the list has more than one element:
                - Create a new list of length n - 1.
                - For each index i (0 <= i < n - 1), set newNums[i] = (nums[i] + nums[i+1]) % 10.
                - Replace nums with newNums.
            2. Return the single remaining element.

        Args:
            nums (List[int]): List of digits (0-9).

        Returns:
            int: The triangular sum of the list.

        Example:
            >>> triangularSum([1,2,3,4,5])
            8

        Time Complexity: O(n^2), where n is the length of nums.
        Space Complexity: O(n), for storing intermediate lists.
        """
        while len(nums) > 1:
            curr = [0] * (len(nums) - 1)

            for i in range(len(curr)):
                curr[i] = (nums[i] + nums[i + 1]) % 10

            nums = curr

        return nums[0]
