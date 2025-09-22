class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Given an integer list nums (0-indexed), and two integers target and start,
        find the minimum distance between start and any index i such that nums[i] == target.

        The distance is defined as abs(i - start). It is guaranteed that target exists in nums.

        Args:
            nums (List[int]): The input list of integers.
            target (int): The target value to search for in nums.
            start (int): The starting index.

        Returns:
            int: The minimum distance between start and any index i where nums[i] == target.

        Example:
            >>> getMinDistance([1,2,3,4,5], 5, 3)
            1

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        min_dist = 10**5

        for i in range(len(nums)):
            if nums[i] == target:
                curr_dist = abs(i - start)
                if curr_dist < min_dist:
                    min_dist = curr_dist

        return min_dist
