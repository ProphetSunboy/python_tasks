class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        """
        Given a 0-indexed integer list `nums` and an integer `k`, return the sum
        of elements in `nums` whose indices have exactly `k` set bits in their binary representation.

        A set bit in an integer is a '1' in its binary representation.
        For example, the binary representation of 21 is 10101, which has 3 set bits.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The required number of set bits in the index.

        Returns:
            int: The sum of elements at indices with exactly `k` set bits.

        Example:
            >>> sumIndicesWithKSetBits([5,10,1,5,2], 1)
            13

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        s = 0

        for i, num in enumerate(nums):
            if i.bit_count() == k:
                s += num

        return s
