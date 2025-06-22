class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        """Calculates the sum of squares of special elements in a list.

        An element is special if its 1-based index divides the lists length.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The sum of the squares of all special elements.

        Example:
            Input: nums = [1, 2, 3, 4]
            Output: 21
            Explanation: The special elements are nums[0], nums[1], and nums[3]
                         because their 1-based indices (1, 2, and 4) divide
                         the list length, n=4.
                         The sum of squares is 1**2 + 2**2 + 4**2 = 21.

        Time complexity: O(N), where N is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        sum_of_squares = 0

        for i, num in enumerate(nums, 1):
            if len(nums) % i == 0:
                sum_of_squares += num**2

        return sum_of_squares
