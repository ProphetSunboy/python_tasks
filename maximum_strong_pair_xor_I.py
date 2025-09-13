class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        """
        Given a 0-indexed integer list nums, find the maximum XOR value among all
        strong pairs in the list.

        A pair of integers x and y is called a strong pair if:
            |x - y| <= min(x, y)

        You may select the same integer twice to form a pair.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The maximum XOR value among all strong pairs in nums.

        Examples:
            >>> maximumStrongPairXor([1, 2, 3])
            3
            >>> maximumStrongPairXor([5, 6, 7, 8])
            15

        Time Complexity: O(n^2), where n is the length of nums.
        Space Complexity: O(1)

        LeetCode: Beats 98.34% of submissions
        """
        max_xor = 0
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] * 2:
                    break

                if nums[i] ^ nums[j] > max_xor:
                    max_xor = nums[i] ^ nums[j]

        return max_xor
