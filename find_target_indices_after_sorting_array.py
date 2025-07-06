class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """Find all target indices after sorting the list in non-decreasing order.

        A target index is an index i such that nums[i] == target after sorting.

        Args:
            nums (list[int]): A 0-indexed integer list to search in.
            target (int): The target element to find indices for.

        Returns:
            list[int]: A list of target indices sorted in increasing order.
                      Returns empty list if target is not found.

        Example:
            >>> targetIndices([1,2,5,2,3], 2)
            [1, 2]
            >>> targetIndices([1,2,5,2,3], 3)
            [3]
            >>> targetIndices([1,2,5,2,3], 6)
            []

        Time complexity: O(n log n) due to sorting
        Space complexity: O(n) for storing the result list

        LeetCode: Beats 100% of submissions
        """
        if target not in nums:
            return []

        nums.sort()
        res = []

        for i in range(nums.index(target), len(nums)):
            if nums[i] == target:
                res.append(i)
            else:
                break

        return res
