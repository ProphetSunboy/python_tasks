class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        """
        Returns the minimum number of adjacent swaps required to make a given 0-indexed permutation semi-ordered.

        A permutation is semi-ordered if the first element is 1 and the last element is n (where n is the length of nums).
        You may swap any two adjacent elements any number of times.

        Args:
            nums (List[int]): A 0-indexed permutation of integers from 1 to n.

        Returns:
            int: The minimum number of adjacent swaps needed to make nums semi-ordered.

        Example:
            >>> semiOrderedPermutation([2, 1, 4, 3])
            2
            >>> semiOrderedPermutation([1, 3, 4, 2, 5])
            0

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        one_pos = -1
        n_pos = -1

        for i, num in enumerate(nums):
            if num == 1:
                one_pos = i
            elif num == len(nums):
                n_pos = i

        if one_pos > n_pos:
            return one_pos + len(nums) - n_pos - 2

        return one_pos + len(nums) - n_pos - 1
