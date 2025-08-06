class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        """
        Applies a sequence of operations to a 0-indexed list of non-negative integers.

        For each index i from 0 to n-2:
            - If nums[i] == nums[i + 1], set nums[i] = 2 * nums[i] and nums[i + 1] = 0.
            - Otherwise, do nothing.
        After all operations, shift all zeros in the list to the end, preserving the order of non-zero elements.

        Args:
            nums (list[int]): The input list of non-negative integers.

        Returns:
            list[int]: The resulting list after applying the operations and shifting zeros to the end.

        Example:
            >>> applyOperations([1,2,2,1,1,0])
            [1,4,2,0,0,0]
            >>> applyOperations([1,0,2,0,0,1])
            [1,2,1,0,0,0]

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        res = []
        zeros = 0

        for i in range(len(nums) - 1):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == nums[i + 1]:
                res.append(nums[i] * 2)
                nums[i + 1] = 0
            else:
                res.append(nums[i])

        if nums[-1] == 0:
            zeros += 1
        else:
            res.append(nums[-1])

        return res + [0] * zeros
