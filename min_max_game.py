class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        """
        Given a 0-indexed integer list nums whose length is a power of 2,
        repeatedly apply the following process until one number remains:

        1. If the length of nums is 1, return the single element.
        2. Otherwise, create a new list new_nums of length n // 2.
           - For every even index i (0-based) in new_nums, set new_nums[i] = min(nums[2 * i], nums[2 * i + 1]).
           - For every odd index i in new_nums, set new_nums[i] = max(nums[2 * i], nums[2 * i + 1]).
        3. Replace nums with new_nums and repeat.

        Args:
            nums (List[int]): Input list of integers, length is a power of 2.

        Returns:
            int: The last remaining number after applying the algorithm.

        Example:
            >>> minMaxGame([1, 3, 5, 2, 4, 8, 2, 2])
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), due to the creation of new lists at each step.

        LeetCode: Beats 100% of submissions
        """
        while len(nums) > 1:
            new_nums = []

            for i in range(0, len(nums), 2):
                if len(new_nums) % 2 == 0:
                    new_nums.append(min(nums[i], nums[i + 1]))
                else:
                    new_nums.append(max(nums[i], nums[i + 1]))

            nums = new_nums

        return nums[0]
