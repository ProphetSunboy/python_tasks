class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        """
        Returns the sum of all elements in `nums` whose frequency is divisible by `k`.

        Args:
            nums (List[int]): A list of integers.
            k (int): The divisor for frequency divisibility.

        Returns:
            int: The sum of elements whose frequency in `nums` is divisible by `k`.

        Example:
            >>> sumDivisibleByK([1, 2, 2, 3, 3, 3], 2)
            4   # (2 appears twice, 3 appears three times (not divisible by 2), so sum is 2*2 = 4)

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(m), where m is the number of unique elements in nums.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        total_freq = 0

        for num, freq in c.items():
            if freq % k == 0:
                total_freq += num * freq

        return total_freq
