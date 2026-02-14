class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        """
        Given an integer list nums of length n, count the number of dominant
        indices.

        An element at index i is called dominant if:
            nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])

        The average of a set of numbers is obtained by adding all the numbers
        together and dividing by the total count.

        Note:
            The rightmost element of any list is not considered dominant.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The number of dominant indices in nums.

        Example:
            Input: nums = [10, 3, 1, 2]
            Output: 2

        Time Complexity: O(n)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        dominant = 0
        r_sum = sum(nums)
        r_len = len(nums)

        for i in range(len(nums) - 1):
            r_sum -= nums[i]
            r_len -= 1

            if nums[i] > r_sum / r_len:
                dominant += 1

        return dominant
