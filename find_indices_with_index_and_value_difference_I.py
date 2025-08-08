class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        """
        Finds two indices i and j in the list nums such that:
            - abs(i - j) >= indexDifference
            - abs(nums[i] - nums[j]) >= valueDifference

        Returns [i, j] if such indices exist, otherwise returns [-1, -1].
        If multiple pairs exist, returns any one of them.

        Args:
            nums (list[int]): The input integer list.
            indexDifference (int): The minimum required absolute difference between indices.
            valueDifference (int): The minimum required absolute difference between values.

        Returns:
            list[int]: A list containing the indices [i, j] if found, else [-1, -1].

        Example:
            >>> findIndices([1, 5, 2, 8], 2, 4)
            [0, 3]

        Time Complexity: O(n^2), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        for i in range(len(nums)):
            for j in range(i + indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]
