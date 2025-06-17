class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        """Create a target list by inserting numbers at specified indices.

        Given two lists of integers nums and index, creates a target list by inserting
        each number from nums at the corresponding index position in index.

        Args:
            nums (list[int]): List of numbers to insert
            index (list[int]): List of indices where numbers should be inserted

        Returns:
            list[int]: The resulting target list after all insertions

        Examples:
            >>> createTargetArray([0,1,2,3,4], [0,1,2,2,1])
            [0,4,1,3,2]  # Numbers inserted at specified indices
            >>> createTargetArray([1,2,3,4,0], [0,1,2,3,0])
            [0,1,2,3,4]  # Numbers inserted at specified indices

        Time complexity: O(n²) - where n is length of input lists
        Space complexity: O(n) - to store the target list

        LeetCode: Beats 100% of submissions
        """
        target = []

        for num, i in zip(nums, index):
            target.insert(i, num)

        return target
