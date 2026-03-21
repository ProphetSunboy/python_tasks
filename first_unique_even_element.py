class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        """
        Returns the first even integer that appears exactly once in nums.

        An integer x is considered even if it is divisible by 2.
        If no such integer exists, returns -1.

        Args:
            nums (list[int]): The list of integers to search.

        Returns:
            int: The first unique even integer, or -1 if none exists.

        Example:
            Input: nums = [1, 2, 3, 4, 2]
            Output: 4  # 4 is the first even number that appears exactly once

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), due to the use of a counter.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)

        for num in nums:
            if num % 2 == 0 and c[num] == 1:
                return num

        return -1
