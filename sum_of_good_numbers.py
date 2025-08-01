class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        """
        Given a list of integers nums and an integer k, an element nums[i] is considered
        "good" if it is strictly greater than the elements at indices i - k and i + k
        (if those indices exist). If neither of these indices exists, nums[i] is still considered good.

        Returns the sum of all good elements in the list.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The offset for checking neighbors.

        Returns:
            int: The sum of all good elements in nums.

        Example:
            >>> sumOfGoodNumbers([5, 1, 9, 2, 7], 2)
            11

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        good_sum = 0

        for i in range(len(nums)):
            if (i - k < 0 or nums[i] > nums[i - k]) and (
                i + k >= len(nums) or nums[i] > nums[i + k]
            ):
                good_sum += nums[i]

        return good_sum
