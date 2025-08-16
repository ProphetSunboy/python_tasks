class Solution:
    def isGood(self, nums: list[int]) -> bool:
        """
        Determines if the given integer list nums is a 'good' list.

        A list is considered good if it is a permutation of base[n], where:
            base[n] = [1, 2, ..., n-1, n, n]
        That is, the list has length n+1, contains each integer from 1 to n-1 exactly once,
        and contains the integer n exactly twice.

        Args:
            nums (list[int]): The list to check.

        Returns:
            bool: True if nums is a permutation of base[n] for some n, False otherwise.

        Examples:
            >>> isGood([1, 1])
            True
            >>> isGood([1, 2, 3, 3])
            True
            >>> isGood([1, 2, 2, 3])
            False

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        return sorted(nums) == list(range(1, len(nums))) + [len(nums) - 1]
