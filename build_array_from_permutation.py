class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        """Builds a list where each element is the value at the index specified by the corresponding element in the input list.

        Given a zero-based permutation nums (0-indexed), builds an array ans of the same length where
        ans[i] = nums[nums[i]] for each 0 <= i < nums.length.

        A zero-based permutation nums is a list of distinct integers from 0 to nums.length - 1 (inclusive).

        Args:
            nums (List[int]): The input permutation list

        Returns:
            List[int]: The built list where ans[i] = nums[nums[i]]

        Example:
            >>> buildArray([0,2,1,5,3,4])
            [0,1,2,4,5,3]

        Time complexity: O(n) - where n is the length of the input list
        Space complexity: O(n) - for storing the result list

        LeetCode: Beats 100% of submissions
        """
        return [nums[num] for num in nums]
