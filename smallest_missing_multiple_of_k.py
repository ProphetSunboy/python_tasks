class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        """
        Given an integer list nums and an integer k, returns the smallest positive
        multiple of k that does not appear in nums.

        A multiple of k is any positive integer that is divisible by k.

        Args:
            nums (List[int]): The list of integers to check against.
            k (int): The positive integer whose multiples are being considered.

        Returns:
            int: The smallest missing positive multiple of k.

        Example:
            >>> missingMultiple([2, 4, 6, 8], 2)
            10

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        nums_s = set(nums)
        smallest = k

        while smallest in nums_s:
            smallest += k

        return smallest
